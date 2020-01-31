from autodcf.models.dcf import DCF


class SimpleDCF(DCF):
    """Creates simple DCF that uses past percentages to sales as baseline for future growth.

    Simplifying Assumptions:
        - COGS, SGA, Depreciation, Amortization, Interest,
        and CapEx stay at constant % relative to sales
        - Change in net working capital / change in sales stays constant
        - Tax rate stays constant
    """

    def __init__(self,
                 company,
                 sales_growth,
                 discount_rate,
                 terminal_growth_rate,
                 change_in_nwc_to_change_in_sales,
                 tax_rate,
                 window=5):
        """

        Args:
            company (autodcf.company.Company): Company object that DCF is for.
            sales_growth (Union[np.array, float, int]): Sales growth. If given iterable,
                its length should be equal to the window size.
            discount_rate (float): The discount rate for the model. Note that 0.1 = 10%.
            terminal_growth_rate: The terminal growth rate for after window. Note that 0.1 = 10%.
            window: Number of periods until terminal value.
                Defaults to 5.
        """
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
                         tax_rate=tax_rate,  # Needs value
                         capex_to_sales=company.cash_flows.capex / company.income_statement.sales,
                         change_in_nwc_to_change_in_sales=change_in_nwc_to_change_in_sales)  # noqa:E501
