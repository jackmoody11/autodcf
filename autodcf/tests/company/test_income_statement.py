import pytest

from datetime import datetime

from autodcf.company import IncomeStatement


@pytest.fixture(scope='class')
def income_statement():
    return IncomeStatement(sales=100,
                           cogs=50,
                           sga=20,
                           rd=0,
                           depreciation=3,
                           amortization=2,
                           interest=0,
                           nonrecurring_cost=5,
                           tax=5,
                           start_date=datetime(2019, 1, 1),
                           end_date=datetime(2020, 1, 1))


class TestIncomeStatement:
    def test_sales(self, income_statement):
        assert income_statement.sales == 100

    def test_set_sales(self, income_statement):
        income_statement.sales = 105
        assert income_statement.sales == 105

    def test_cogs(self, income_statement):
        assert income_statement.cogs == 50

    def test_set_cogs(self, income_statement):
        income_statement.cogs = 55
        assert income_statement.cogs == 55

    def test_sga(self, income_statement):
        assert income_statement.sga == 20

    def test_set_sga(self, income_statement):
        income_statement.sga = 23
        assert income_statement.sga == 23

    def test_nonrecurring_cost(self, income_statement):
        assert income_statement.nonrecurring_cost == 5

    def test_set_nonrecurring_cost(self, income_statement):
        income_statement.nonrecurring_cost = 0
        assert income_statement.nonrecurring_cost == 0

    def test_tax(self, income_statement):
        assert income_statement.tax == 5

    def test_set_tax(self, income_statement):
        income_statement.tax = 6
        assert income_statement.tax == 6

    def test_depreciation(self, income_statement):
        assert income_statement.depreciation == 3

    def test_set_depreciation(self, income_statement):
        income_statement.depreciation = 3.5
        assert income_statement.depreciation == 3.5

    def test_amortization(self, income_statement):
        assert income_statement.amortization == 2

    def test_set_amortization(self, income_statement):
        income_statement.amortization = 2.3
        assert income_statement.amortization == 2.3

    def test_set_rd(self, income_statement):
        income_statement.rd = 2000
        assert income_statement.rd == 2000

    def test_set_interest(self, income_statement):
        income_statement.interest = 100
        assert income_statement.interest == 100

    def test_start_date(self, income_statement):
        assert income_statement.start_date == datetime(2019, 1, 1)

    def test_end_date(self, income_statement):
        assert income_statement.end_date == datetime(2020, 1, 1)

    def test_end_date_after_start_date(self):
        with pytest.raises(ValueError):
            return IncomeStatement(sales=0,
                                   cogs=0,
                                   sga=0,
                                   rd=0,
                                   depreciation=0,
                                   amortization=0,
                                   nonrecurring_cost=0,
                                   interest=0,
                                   tax=0,
                                   start_date=datetime(2020, 3, 3),
                                   end_date=datetime(2020, 1, 1))
