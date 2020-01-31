import pytest

from autodcf.company import BalanceSheet, CashFlows, Company, IncomeStatement


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
