import numpy as np
import pytest

from autodcf.models import SimpleDCF


class TestSimpleDCF:

    def test_sales_growth(self, simple_dcf):
        assert (simple_dcf.sales_growth == np.repeat(0.03, 5)).all()

    def test_discount_rate(self, simple_dcf):
        assert simple_dcf.discount_rate == 0.14

    def test_terminal_growth_rate(self, simple_dcf):
        assert simple_dcf.terminal_growth_rate == 0.03

    def test_window(self, simple_dcf):
        assert simple_dcf.window == 5

    def test_forecast_sales(self, simple_dcf):
        forecast = simple_dcf.forecast()
        assert forecast.loc[-1, 'Sales'] == 100
        assert forecast.loc[0, 'Sales'] == 100 * (1 + simple_dcf.sales_growth)
