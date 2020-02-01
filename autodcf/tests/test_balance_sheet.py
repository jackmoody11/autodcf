import pytest

from autodcf.company import BalanceSheet


@pytest.fixture(scope='class')
def balance_sheet():
    return BalanceSheet(assets=100,
                        liabilities=55)


class TestBalanceSheet:

    def test_assets(self, balance_sheet):
        assert balance_sheet.assets == 100

    def test_set_assets(self, balance_sheet):
        balance_sheet.assets = 90
        assert balance_sheet.assets == 90

    def test_liabilities(self, balance_sheet):
        assert balance_sheet.liabilities == 55

    def test_set_liabilities(self, balance_sheet):
        balance_sheet.liabilities = 57.5
        assert balance_sheet.liabilities == 57.5

    def test_equity(self):
        bs = BalanceSheet(assets=75, liabilities=30)
        assert bs.equity == 45
        bs.assets = 70
        assert bs.equity == 40

    def test_debt_to_equity(self, balance_sheet):
        bs = BalanceSheet(assets=400, liabilities=300)
        assert bs.debt_to_equity == 3.0

    def test_date(self, balance_sheet):
        from datetime import datetime
        assert balance_sheet.date is None
        balance_sheet.date = datetime(2019, 1, 1)
        assert balance_sheet.date.year == 2019
        assert balance_sheet.date.month == 1
        assert balance_sheet.date.day == 1

    def test_set_date(self, balance_sheet):
        from datetime import datetime
        balance_sheet.date = datetime(2020, 1, 1)
        assert balance_sheet.date == datetime(2020, 1, 1)
