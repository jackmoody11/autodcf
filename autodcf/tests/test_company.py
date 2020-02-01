import pytest


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

    def test_set_cash_flows(self, company, income_statement, balance_sheet):
        """Cash flows should only be CashFlow object."""
        with pytest.raises(TypeError):
            company.cash_flows = income_statement
        with pytest.raises(TypeError):
            company.cash_flows = balance_sheet

    def test_set_income_statement(self, company, balance_sheet, cash_flows):
        with pytest.raises(TypeError):
            company.income_statement = balance_sheet
        with pytest.raises(TypeError):
            company.income_statement = cash_flows

    def test_set_price_per_share(self, company):
        company.price_per_share = 100
        assert company.price_per_share == 100

    def test_set_fully_diluted_shares(self, company):
        company.fully_diluted_shares = 1000
        assert company.fully_diluted_shares == 1000

    def test_set_balance_sheet(self, company, cash_flows, income_statement):
        from autodcf.company import BalanceSheet
        new_balance_sheet = BalanceSheet(assets=2000, liabilities=1500)
        company.balance_sheet = new_balance_sheet
        assert company.balance_sheet.assets == 2000
        assert company.balance_sheet.liabilities == 1500

        with pytest.raises(TypeError):
            company.balance_sheet = cash_flows
        with pytest.raises(TypeError):
            company.balance_sheet = income_statement
