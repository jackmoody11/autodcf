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

    def test_get_sales(self, simple_dcf):
        expected = np.array([73.5, 77.175, 81.03375, 85.0854375, 89.33970938, 93.80669484,
                             98.49702959])
        # assert (simple_dcf.get_sales() - expected < 1e-4).all()  # Test that sales numbers are close
        pass
