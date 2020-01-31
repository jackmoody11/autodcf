import pytest

from autodcf.company import BalanceSheet, CashFlows, IncomeStatement, Company


@pytest.fixture(scope='session')
def balance_sheet():
    return BalanceSheet(assets=100,
                        liabilities=50)


@pytest.fixture(scope='session')
def cash_flows():
    return CashFlows(capex=3)


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
def company(balance_sheet, cash_flows, income_statement):
    return Company(fully_diluted_shares=10,
                   price_per_share=5.75,
                   balance_sheet=balance_sheet,
                   cash_flows=cash_flows,
                   income_statement=income_statement)
