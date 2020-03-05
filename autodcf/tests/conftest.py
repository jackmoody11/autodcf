import pytest

from autodcf.company import BalanceSheet, CashFlows, IncomeStatement, Company
from autodcf.models import SimpleDCF


@pytest.fixture
def balance_sheet():
    return BalanceSheet(
        cash=10,
        short_term_investments=10,
        net_receivables=10,
        inventory=5,
        other_current_assets=5,
        ppe=30,
        goodwill=10,
        intangible_assets=20,
        other_lt_assets=0,
        accounts_payable=5,
        accrued_liabilities=9,
        short_term_debt=6,
        current_part_lt_debt=4,
        long_term_debt=14,
        other_current_liabilities=2,
        other_lt_liabilities=2,
        deferred_lt_liabilities=3,
        minority_interest=5,
        other_lt_liability_debt_multiplier=1)


@pytest.fixture
def cash_flows():
    return CashFlows(capex=3)


@pytest.fixture
def income_statement():
    return IncomeStatement(sales=100,
                           cogs=50,
                           sga=25,
                           rd=2,
                           depreciation=4,
                           amortization=2,
                           interest=1,
                           nonrecurring_cost=3,
                           tax=4)


@pytest.fixture
def company(balance_sheet, cash_flows, income_statement):
    return Company(fully_diluted_shares=10,
                   price_per_share=5.75,
                   balance_sheet=balance_sheet,
                   cash_flows=cash_flows,
                   income_statement=income_statement)


@pytest.fixture
def simple_dcf(company):
    return SimpleDCF(change_in_nwc_to_change_in_sales=0.1,
                     company=company,
                     discount_rate=0.14,
                     sales_growth=0.03,
                     tax_rate=0.21,
                     terminal_growth_rate=0.03,
                     window=5)
