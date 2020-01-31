import numpy as np
import pytest

from autodcf.models import DCF, SimpleDCF


@pytest.fixture
def simple_dcf(company):
    return SimpleDCF(change_in_nwc_to_change_in_sales=0.1,
                     company=company,
                     discount_rate=0.14,
                     sales_growth=0.03,
                     tax_rate=0.21,
                     terminal_growth_rate=0.03,
                     window=5)


class TestDCF:

    def test_company(self, simple_dcf, company):
        assert simple_dcf.company is company

    def test_sales_growth(self, simple_dcf):
        assert (simple_dcf.sales_growth == np.repeat(0.03, 5)).all()

    def test_discount_rate(self, simple_dcf):
        assert simple_dcf.discount_rate == 0.14

    def test_terminal_growth_rate(self, simple_dcf):
        assert simple_dcf.terminal_growth_rate == 0.03

    def test_window(self, simple_dcf):
        assert simple_dcf.window == 5

    # TODO: Test if forecasted DataFrame is correct (just look at discounted cash flows)
    def test_forecast(self, simple_dcf):
        pass
