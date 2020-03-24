import pytest

from autodcf.company import BalanceSheet


class TestBalanceSheet:

    def test_assets(self, balance_sheet):
        assert balance_sheet.assets == 100

    def test_liabilities(self, balance_sheet):
        assert balance_sheet.liabilities == 50

    def test_equity(self, balance_sheet):
        assert balance_sheet.equity == 50

    def test_current_assets(self, balance_sheet):
        assert balance_sheet.current_assets == 40

    def test_long_term_assets(self, balance_sheet):
        assert balance_sheet.long_term_assets == 60

    def test_debt_to_equity(self, balance_sheet):
        assert balance_sheet.debt_to_equity == 1.0

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

    def test_bad_date(self, balance_sheet):
        from datetime import datetime
        with pytest.raises(TypeError):
            balance_sheet.date = "20150101"

    def test_net_debt(self, balance_sheet):
        assert balance_sheet.net_debt == 2
