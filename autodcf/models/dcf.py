import numpy as np
import pandas as pd

from autodcf.models._base import AbstractDCF
from datetime import datetime


class DCF(AbstractDCF):
    """Class for flexible DCF.

    Note that all _to_sales args take either an iterable or float. If given a float, the DCF will
    use this constant across all time periods (ex: if given 0.45 for COGS, COGS will be 45% of sales
    for all forecasted periods). If given iterable, the first value will be the value used for the first
    year in the forecast and the last value will be the value used in the terminal year.

    Args:
        company (autodcf.company.Company): Company to do DCF analysis for.
        sales_growth (Union[Iterable, float]): Iterable of sales growth numbers to iterate over or constant growth rate.
            Values are in order, so first value in iterable applies to next sales period and
            last value applies to last sales period in DCF. Note, if you want to have 5% sales growth, use 0.05.
        discount_rate (float): Rate at which cash flow should be discounted.
        terminal_growth_rate (float): Rate at which sales are estimated to grow after returning to normal profit levels.
        window (int): Number of years until company returns to normal profit margins (terminal year).
        cogs_to_sales (Union[Iterable, float]): COGS as % of sales.
        sga_to_sales (Union[Iterable, float]): SGA as % of sales.
        rd_to_sales (Union[Iterable, float]): R&D as % of sales.
        da_to_sales (Union[Iterable, float]): Depreciation & amortization as % of sales. Assumes amortization is tax
            deductible.
        interest_to_sales (Union[Iterable, float]): Interest as % of sales.
        tax_rate (float): Tax rate.
        capex_to_sales (Union[Iterable, float]): Capex as % of sales.
        change_in_nwc_to_change_in_sales (float): Ratio of how much net working capital must change to increase sales by
            1 unit.
    """

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
                 change_in_nwc_to_change_in_sales,
                 terminal_discount_rate=None):
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
        self._forecast = pd.DataFrame(index=np.arange(-1, self.window + 1))
        self._terminal_discount_rate = discount_rate if terminal_discount_rate is None else terminal_discount_rate

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
    def terminal_discount_rate(self):
        """Discount rate after terminal year."""
        return self._terminal_discount_rate

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
        """Cost of goods sold as a percentage of sales."""
        return self._cogs_to_sales

    @property
    def sga_to_sales(self):
        """Selling, general, and administrative costs as a percentage of sales."""
        return self._sga_to_sales

    @property
    def rd_to_sales(self):
        """Research and development costs as a percentage of sales."""
        return self._rd_to_sales

    @property
    def da_to_sales(self):
        """Depreciation and amortization as a percentage of sales."""
        return self._da_to_sales

    @property
    def interest_to_sales(self):
        """Interest expense as a percentage of sales."""
        return self._interest_to_sales

    @property
    def tax_rate(self):
        """Effective tax rate for company."""
        return self._tax_rate

    @property
    def capex_to_sales(self):
        """Capital expenditures as a percentage of sales."""
        return self._capex_to_sales

    @property
    def change_in_nwc_to_change_in_sales(self):
        """How much net working capital is expected to need to increase for each dollar increase in sales."""
        return self._change_in_nwc_to_change_in_sales

    def _calculate_sales(self):
        """Calculate sales for window of growth.

        Returns:
            Numpy array with sales from each period in order.
        """
        sales_growth = np.repeat(self.sales_growth, self.window + 1) if isinstance(self.sales_growth,
                                                                                   float) else self.sales_growth
        initial_sales = self.company.income_statement.sales
        return np.concatenate(([initial_sales], initial_sales * np.cumprod(1 + sales_growth)))

    def _multiply_by_sales_percent(self, percent_of_sales):
        """Find values for stat in all periods given percent of sales stat accounts for.

        Returns:
            Pandas series with statistic multiplied by forecast Sales values.
        """
        return self._forecast['Sales'] * percent_of_sales

    def _calculate_free_cash_flow(self):
        """Calculate free cash flow for each period.

        Returns:
            Pandas Series with free cash flow for each period in forecast.
        """
        return self._forecast['Net Income'] + self._forecast['D&A'] - self._forecast['Capex'] - self._forecast[
            'Change in NWC']

    def _discount_cash_flows(self):
        """Discount cash flows at given discount rate."""
        discount_factors = np.array([1 / (1 + self.discount_rate) ** i for i in range(self.window + 1)])
        return self._forecast.loc[0:, 'FCF'] * discount_factors

    def forecast(self):
        """Get pandas dataframe with all info needed to complete forecast.

        Returns:
            forecast (pd.DataFrame): Pandas data frame with forecasted future income statements and discounted
                free cash flows.
        """
        self._forecast['Year'] = np.arange(datetime.now().year - 1, datetime.now().year + self.window + 1)
        self._forecast['Sales'] = self._calculate_sales()
        self._forecast['COGS'] = self._multiply_by_sales_percent(self.cogs_to_sales)
        self._forecast['Gross Profit'] = self._forecast['Sales'] - self._forecast['COGS']
        self._forecast['SG&A'] = self._multiply_by_sales_percent(self.sga_to_sales)
        self._forecast['Operating Profit'] = self._forecast['Gross Profit'] - self._forecast['SG&A']
        self._forecast['R&D'] = self._multiply_by_sales_percent(self.rd_to_sales)
        self._forecast['EBITDA'] = self._forecast['Operating Profit'] - self._forecast['R&D']
        self._forecast['D&A'] = self._multiply_by_sales_percent(self.da_to_sales)
        self._forecast['EBIT'] = self._forecast['EBITDA'] - self._forecast['D&A']  # noqa:E501
        self._forecast['Interest'] = self._multiply_by_sales_percent(self.interest_to_sales)
        self._forecast['EBT'] = self._forecast['EBIT'] - self._forecast['Interest']
        self._forecast['Taxes'] = self._forecast['EBT'] * self.tax_rate
        self._forecast.loc[-1, 'Taxes'] = self.company.income_statement.tax
        self._forecast['Net Income'] = self._forecast['EBT'] - self._forecast['Taxes']
        self._forecast['Capex'] = self._multiply_by_sales_percent(self.capex_to_sales)
        # ΔSales * ΔNWC/ΔSales = ΔNWC
        change_in_sales = np.diff(self._forecast['Sales'])
        future_changes_nwc = change_in_sales * self.change_in_nwc_to_change_in_sales
        self._forecast['Change in NWC'] = np.concatenate(([0.0], future_changes_nwc))
        self._forecast['FCF'] = self._calculate_free_cash_flow()
        self._forecast['Discounted FCF'] = self._discount_cash_flows()
        return self._forecast

    @property
    def enterprise_value(self):
        """Enterprise value given by discounted cash flow analysis."""
        return self.discounted_window_cash_flow + self.discounted_terminal_cash_flow

    @property
    def equity_value(self):
        """Returns total equity value of firm."""
        return self.enterprise_value - self.company.balance_sheet.net_debt

    @property
    def equity_value_per_share(self):
        """Equity value divided by total number of shares outstanding."""
        return self.equity_value / self.company.fully_diluted_shares

    @property
    def discounted_terminal_cash_flow(self):
        """Sum of discounted cash flows after window."""
        f = self.forecast()
        last_fcf = f.loc[self.window, 'Discounted FCF']
        terminal_discount_minus_growth = (self.terminal_discount_rate - self.terminal_growth_rate)
        tv_discounted_to_window = last_fcf * (1 + self.terminal_growth_rate) / terminal_discount_minus_growth
        return tv_discounted_to_window / (1 + self.discount_rate) ** self.window

    @property
    def discounted_window_cash_flow(self):
        """Add up discounted cash flows from window."""
        f = self.forecast()
        return f.loc[0:, 'Discounted FCF'].sum()

    @property
    def absolute_upside_per_share(self):
        return self.equity_value_per_share - self.company.price_per_share

    @property
    def percent_upside_per_share(self):
        return self.absolute_upside_per_share / self.company.price_per_share
