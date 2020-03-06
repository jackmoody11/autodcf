import pytest


@pytest.fixture
def replacement_balance_sheet():
    from autodcf.company import BalanceSheet
    # Assets = 11,000
    #   Current = 5,000
    #   Long term = 6,000
    # Liabilities = 5,000
    #   Current = 4,000
    #   Long term = 1,000
    return BalanceSheet(cash=1000,
                        short_term_investments=1000,
                        net_receivables=2000,
                        inventory=500,
                        other_current_assets=500,
                        ppe=3000,
                        goodwill=1000,
                        intangible_assets=2000,
                        other_lt_assets=0,
                        accounts_payable=500,
                        accrued_liabilities=900,
                        short_term_debt=600,
                        current_part_lt_debt=400,
                        other_current_liabilities=1600,
                        long_term_debt=0,
                        other_lt_liabilities=200,
                        deferred_lt_liabilities=300,
                        minority_interest=500)


@pytest.fixture
def replacement_income_statement():
    from autodcf.company import IncomeStatement
    return IncomeStatement(sales=1000,
                           cogs=300,
                           sga=200,
                           rd=50,
                           depreciation=10,
                           amortization=5,
                           nonrecurring_cost=30,
                           interest=15,
                           tax=200)


@pytest.fixture
def replacement_cash_flows():
    from autodcf.company import CashFlows
    return CashFlows(capex=300)


class TestCompany:
    def test_fully_diluted_shares(self, company):
        assert company.fully_diluted_shares == 10

    def test_price_per_share(self, company):
        assert company.price_per_share == 5.75

    def test_balance_sheet(self, company, balance_sheet):
        assert company.balance_sheet is balance_sheet

    def test_cash_flows(self, company, cash_flows):
        assert company.cash_flows is cash_flows

    def test_income_statement(self, company, income_statement):
        assert company.income_statement is income_statement

    def test_set_bad_cash_flows(self, company, income_statement, balance_sheet):
        """Cash flows should only be CashFlow object."""
        with pytest.raises(TypeError):
            company.cash_flows = income_statement
        with pytest.raises(TypeError):
            company.cash_flows = balance_sheet

    def test_set_good_cash_flows(self, company, cash_flows, replacement_cash_flows):
        assert company.cash_flows == cash_flows
        company.cash_flows = replacement_cash_flows
        assert company.cash_flows == replacement_cash_flows

    def test_set_bad_income_statement(self, company, balance_sheet, cash_flows):
        with pytest.raises(TypeError):
            company.income_statement = balance_sheet
        with pytest.raises(TypeError):
            company.income_statement = cash_flows

    def test_set_good_income_statement(self, company, income_statement, replacement_income_statement):
        assert company.income_statement == income_statement
        company.income_statement = replacement_income_statement
        assert company.income_statement == replacement_income_statement

    def test_set_price_per_share(self, company):
        company.price_per_share = 100
        assert company.price_per_share == 100

    def test_set_fully_diluted_shares(self, company):
        company.fully_diluted_shares = 1000
        assert company.fully_diluted_shares == 1000

    def test_set_balance_sheet(self, company, cash_flows, income_statement, replacement_balance_sheet):
        company.balance_sheet = replacement_balance_sheet
        assert company.balance_sheet.assets == 11000
        assert company.balance_sheet.liabilities == 5000
        assert company.balance_sheet.current_assets == 5000
        assert company.balance_sheet.long_term_assets == 6000
        assert company.balance_sheet.current_liabilites == 4000
        assert company.balance_sheet.long_term_liabilities == 1000

        with pytest.raises(TypeError):
            company.balance_sheet = cash_flows
        with pytest.raises(TypeError):
            company.balance_sheet = income_statement
