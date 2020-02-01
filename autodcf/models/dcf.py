import numpy as np
import pandas as pd

from autodcf.models.base import AbstractDCF
from datetime import datetime


def fill_row(stat, stat_growth_rate):
    """Get all values for stat given growth rate of initial period."""
    return np.concatenate(([stat], stat * np.cumprod(1 + stat_growth_rate)))


def multiply_by_sales_percent(df, percent_of_sales):
    """Find values for stat in all periods given percent of sales stat accounts for."""
    return df['Sales'] * percent_of_sales


def calculate_free_cash_flow(df):
    tax_rates = (df['Taxes'] / df['EBT'])
    return df['EBITDA'] * tax_rates + df['D&A'] * tax_rates - df['Capex'] - df['Change in NWC']


def discount_cash_flows(cash_flows, discount_rate):
    """Discount cash flows at given discount rate."""
    discount_factors = np.array([1 / (1 + discount_rate) ** i for i in range(len(cash_flows))])
    return cash_flows * discount_factors


class DCF(AbstractDCF):

    def __init__(self,
                 company,
                 sales_growth,
                 discount_rate,
                 terminal_growth_rate,
                 window,
                 cogs_to_sales,
                 sga_to_sales,
                 rd_to_sales,
                 da_to_sales,
                 interest_to_sales,
                 tax_rate,
                 capex_to_sales,
                 change_in_nwc_to_change_in_sales):
        self._company = company
        self._sales_growth = sales_growth
        self._discount_rate = discount_rate
        self._terminal_growth_rate = terminal_growth_rate
        self._window = window
        self._cogs_to_sales = cogs_to_sales
        self._sga_to_sales = sga_to_sales
        self._rd_to_sales = rd_to_sales
        self._da_to_sales = da_to_sales
        self._interest_to_sales = interest_to_sales
        self._tax_rate = tax_rate
        self._capex_to_sales = capex_to_sales
        self._change_in_nwc_to_change_in_sales = change_in_nwc_to_change_in_sales
        self._forecast = pd.DataFrame()

    @property
    def company(self):
        """Company object to do DCF for."""
        return self._company

    @property
    def sales_growth(self):
        """Numpy array of sales growth for each year until end of window."""
        return self._sales_growth

    @property
    def discount_rate(self):
        """Discount rate to discount cash flow at."""
        return self._discount_rate

    @property
    def terminal_growth_rate(self):
        """Rate at which sales are expected to grow perpetually."""
        return self._terminal_growth_rate

    @property
    def window(self):
        """Periods of normal sales growth until terminal growth rate takes over."""
        return self._window

    @property
    def cogs_to_sales(self):
        return self._cogs_to_sales

    @property
    def sga_to_sales(self):
        return self._sga_to_sales

    @property
    def rd_to_sales(self):
        return self._rd_to_sales

    @property
    def da_to_sales(self):
        return self._da_to_sales

    @property
    def interest_to_sales(self):
        return self._interest_to_sales

    @property
    def tax_rate(self):
        return self._tax_rate

    @property
    def capex_to_sales(self):
        return self._capex_to_sales

    @property
    def change_in_nwc_to_change_in_sales(self):
        return self._change_in_nwc_to_change_in_sales

    def forecast(self):
        """Get pandas dataframe with all info needed to complete forecast."""
        self._forecast.index = np.arange(-1, self.window + 1)
        self._forecast['Year'] = np.arange(datetime.now().year,
                                           datetime.now().year + self.window + 1)
        self._forecast['Sales'] = fill_row(self.company.income_statement.sales, self.sales_growth)
        self._forecast['COGS'] = multiply_by_sales_percent(self._forecast, self.cogs_to_sales)
        self._forecast['Gross Profit'] = self._forecast['Sales'] - self._forecast['COGS']
        self._forecast['SG&A'] = multiply_by_sales_percent(self._forecast, self.cogs_to_sales)
        self._forecast['Operating Profit'] = self._forecast['Gross Profit'] - self._forecast['SG&A']
        self._forecast['R&D'] = multiply_by_sales_percent(self._forecast, self.rd_to_sales)
        self._forecast['EBITDA'] = self._forecast['Operating Profit'] - self._forecast['R&D']
        self._forecast['D&A'] = multiply_by_sales_percent(self._forecast, self.da_to_sales)
        self._forecast['EBIT'] = self._forecast['EBITDA'] - self._forecast['D&A']  # noqa:E501
        self._forecast['Interest'] = multiply_by_sales_percent(self._forecast,
                                                               self.interest_to_sales)
        self._forecast['EBT'] = self._forecast['EBIT'] - self._forecast['Interest']
        self._forecast['Taxes'] = self._forecast['EBT'] * self.tax_rate
        self._forecast['Net Income'] = self._forecast['EBT'] - self._forecast['Taxes']
        self._forecast['Capex'] = multiply_by_sales_percent(self._forecast, self.capex_to_sales)
        # ΔSales * ΔNWC/ΔSales = ΔNWC
        change_in_sales = np.diff(self._forecast['Sales'])
        self._forecast['Change in NWC'] = change_in_sales * self.change_in_nwc_to_change_in_sales
        self._forecast['FCF'] = calculate_free_cash_flow(self._forecast)
        self._forecast['Discounted FCF'] = discount_cash_flows(self._forecast['FCF'],
                                                               self.discount_rate)
        return self._forecast

    @property
    def value(self):
        """Find value of """
        return self.discounted_window_cash_flow + self.discounted_terminal_cash_flow

    @property
    def discounted_terminal_cash_flow(self):
        """Sum of discounted cash flows after window."""
        forecast = self.forecast()
        last_fcf = forecast.loc['Discounted FCF', window]
        tv_discounted_to_window = last_fcf * self.terminal_growth_rate / (
                self.discount_rate - self.terminal_growth_rate)
        return tv_discounted_to_window / (1 + self.discount_rate) ** self.window

    @property
    def discounted_window_cash_flow(self):
        """Add up discounted cash flows from window."""
        forecast = self.forecast()
        return forecast.loc['Discounted FCF', 0:].sum()
