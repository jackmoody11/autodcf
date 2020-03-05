import pytest

import numpy as np
import pandas as pd

from autodcf.models import SimpleDCF
from autodcf.tests.utils import datapath


@pytest.fixture
def simple_dcf(company):
    return SimpleDCF(change_in_nwc_to_change_in_sales=0.1,
                     company=company,
                     discount_rate=0.14,
                     sales_growth=0.03,
                     tax_rate=0.21,
                     terminal_growth_rate=0.03,
                     window=5)


@pytest.fixture
def expected_dcf_results():
    return pd.read_excel(datapath('simple_dcf.xlsx'), sheet_name='Results', index_col=0, squeeze=True)


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

    def test_forecast(self, simple_dcf, expected_dcf_results):
        assert expected_dcf_results['enterprise_value'] == simple_dcf.enterprise_value
        assert expected_dcf_results['discounted_window_cash_flow'] == simple_dcf.discounted_window_cash_flow
        assert expected_dcf_results['discounted_terminal_cash_flow'] == simple_dcf.discounted_terminal_cash_flow

    def test_equity_value(self, simple_dcf, expected_dcf_results):
        assert expected_dcf_results['equity_value'] == simple_dcf.equity_value
        assert expected_dcf_results['equity_value_per_share'] == simple_dcf.equity_value_per_share

    def test_absolute_upside(self, simple_dcf, expected_dcf_results):
        assert expected_dcf_results['absolute_upside_per_share'] == simple_dcf.absolute_upside_per_share

    def test_percent_upside(self, simple_dcf, expected_dcf_results):
        assert expected_dcf_results['percent_upside_per_share'] == simple_dcf.percent_upside_per_share
