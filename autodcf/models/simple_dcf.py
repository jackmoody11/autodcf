from autodcf.models.dcf import DCF


class SimpleDCF(DCF):
    """Creates simple DCF that uses past percentages to sales as baseline for future growth.

    Simplifying Assumptions:
        - COGS, SGA, Depreciation, Amortization, Interest,
        and CapEx stay at constant % relative to sales
        - Change in net working capital / change in sales stays constant
        - Tax rate stays constant over entire period

    Args:
        company (autodcf.company.Company): Company to do DCF analysis for.
        sales_growth (Union[Iterable, float]): Iterable of sales growth numbers to iterate over or constant growth rate.
            Values are in order, so first value in iterable applies to next sales period and
            last value applies to last sales period in DCF. Note, if you want to have 5% sales growth, use 0.05.
        discount_rate (float): Rate at which cash flow should be discounted.
        terminal_growth_rate (float): Rate at which sales are estimated to grow after returning to normal profit levels.
        change_in_nwc_to_change_in_sales (float): Ratio of how much net working capital must change to increase sales by
            1 unit.
        tax_rate (float): Tax rate.
        window (int): Number of years until company returns to normal profit margins (terminal year).
    """

    def __init__(self,
                 company,
                 sales_growth,
                 discount_rate,
                 terminal_growth_rate,
                 change_in_nwc_to_change_in_sales,
                 tax_rate,
                 window=5):
        super().__init__(company=company,
                         sales_growth=sales_growth,
                         discount_rate=discount_rate,
                         terminal_growth_rate=terminal_growth_rate,
                         window=window,
                         cogs_to_sales=company.income_statement.cogs / company.income_statement.sales,  # noqa:E501
                         sga_to_sales=company.income_statement.sga / company.income_statement.sales,  # noqa:E501
                         rd_to_sales=company.income_statement.rd / company.income_statement.sales,  # noqa:E501
                         da_to_sales=company.income_statement.da / company.income_statement.sales,  # noqa:E501
                         interest_to_sales=company.income_statement.interest / company.income_statement.sales,
                         tax_rate=tax_rate,
                         capex_to_sales=company.cash_flows.capex / company.income_statement.sales,
                         change_in_nwc_to_change_in_sales=change_in_nwc_to_change_in_sales)  # noqa:E501
