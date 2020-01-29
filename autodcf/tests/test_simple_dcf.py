import numpy as np
import pytest

from autodcf.company import BalanceSheet, CashFlows, Company, IncomeStatement
from autodcf.models.simple_dcf import SimpleDCF


@pytest.fixture(scope='module')
def balance_sheet():
    return BalanceSheet(assets=200,
                        liabilities=40)


@pytest.fixture(scope='module')
def cash_flows():
    return CashFlows(capex=2)


@pytest.fixture(scope='module')
def income_statement():
    return IncomeStatement(sales=70,
                           cogs=20,
                           sga=17,
                           rd=2,
                           depreciation=3,
                           amortization=2,
                           interest=0,
                           nonrecurring_cost=3,
                           tax=6)


@pytest.fixture(scope='class')
def company(balance_sheet, cash_flows, income_statement):
    return Company(fully_diluted_shares=20,
                   price_per_share=5.00,
                   balance_sheet=balance_sheet,
                   cash_flows=cash_flows,
                   income_statement=income_statement)


@pytest.fixture(scope='class')
def simple_dcf(company):
    return SimpleDCF(company=company,
                     sales_growth=0.05,
                     discount_rate=0.12,
                     terminal_growth_rate=0.04,
                     window=7)


@pytest.mark.usefixtures('balance_sheet', 'cash_flows', 'company', 'income_statement')
class TestSimpleDCF:

    def test_sales_growth(self, simple_dcf):
        assert (simple_dcf.sales_growth == np.array([0.05] * 7)).all()

    def test_discount_rate(self, simple_dcf):
        assert simple_dcf.discount_rate == 0.12

    def test_terminal_growth_rate(self, simple_dcf):
        assert simple_dcf.terminal_growth_rate == 0.04

    def test_window(self, simple_dcf):
        assert simple_dcf.window == 7

    def test_get_sales(self, simple_dcf):
        expected = np.array([73.5, 77.175, 81.03375, 85.0854375, 89.33970938, 93.80669484,
                             98.49702959])
        assert (simple_dcf.get_sales() - expected < 1e-4).all()  # Test that sales numbers are close
