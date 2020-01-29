import pytest

from autodcf.company import BalanceSheet, CashFlows, Company, IncomeStatement


@pytest.fixture(scope='module')
def balance_sheet():
    return BalanceSheet(assets=100,
                        liabilities=50)


@pytest.fixture(scope='module')
def cash_flows():
    return CashFlows(capex=3)


@pytest.fixture(scope='module')
def income_statement():
    return IncomeStatement(sales=100,
                           cogs=50,
                           sga=25,
                           rd=0,
                           depreciation=4,
                           amortization=2,
                           interest=0,
                           nonrecurring_cost=3,
                           tax=4)


@pytest.fixture(scope='class')
def company(balance_sheet, cash_flows, income_statement):
    return Company(fully_diluted_shares=10,
                   price_per_share=5.75,
                   balance_sheet=balance_sheet,
                   cash_flows=cash_flows,
                   income_statement=income_statement)


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
