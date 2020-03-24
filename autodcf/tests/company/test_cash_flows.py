import pytest

from autodcf.company import CashFlows


@pytest.fixture(scope='class')
def cash_flows():
    return CashFlows(capex=30)


class TestCashFlows:
    def test_capex(self, cash_flows):
        assert cash_flows.capex == 30

    def test_set_capex(self, cash_flows):
        cash_flows.capex = 25
        assert cash_flows.capex == 25
