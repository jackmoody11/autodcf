import datetime


def now(offset=0):
    """Utility for getting current time or current time minus offset number of years.

    Args:
        offset (int): Number of years to subtract from current year. Defaults to 0.

    Returns:
        date (datetime.datetime): Date offset from today by offset number of years (or today if offset is None).
    """
    n = datetime.datetime.now()
    return n.replace(year=n.year - offset)


class IncomeStatement:
    """Income statement object for specific company during a specific time period.

    Args:
        sales (Union[float, int]): Sales from period.
        cogs (Union[float, int]): Cost of goods sold from period.
        sga (Union[float, int]): Selling, General, and Administrative costs from period.
        rd (Union[float, int]): Research & Development costs from period.
        depreciation (Union[float, int]): Depreciation from period.
        amortization (Union[float, int]): Amortization from period.
        nonrecurring_cost (Union[float, int]): Non-recurring cost from period.
        interest (Union[float, int]): Interest expense from period.
        tax (Union[float, int]): Tax (as absolute currency amount, NOT as tax rate %).
        start_date (datetime.datetime): First day of period for income statement.
        end_date (datetime.datetime): Last day of period for income statement.
    """

    def __init__(self,
                 sales,
                 cogs,
                 sga,
                 rd,
                 depreciation,
                 amortization,
                 nonrecurring_cost,
                 interest,
                 tax,
                 start_date=now(offset=1),
                 end_date=now()):
        self._sales = sales
        self._cogs = cogs
        self._sga = sga
        self._rd = rd
        self._nonrecurring_cost = nonrecurring_cost
        self._interest = interest
        self._tax = tax
        self._depreciation = depreciation
        self._amortization = amortization
        self._start_date = start_date
        if start_date < end_date:
            self._end_date = end_date
        else:
            raise ValueError("End date must be after start date. "
                             "Given start date {0} and end date {1}".format(start_date, end_date))

    @property
    def sales(self):
        """Sales from period."""
        return self._sales

    @sales.setter
    def sales(self, val):
        self._sales = val

    @property
    def cogs(self):
        """Cost of goods sold from period."""
        return self._cogs

    @cogs.setter
    def cogs(self, val):
        self._cogs = val

    @property
    def sga(self):
        """Selling, general, and administrative costs from period."""
        return self._sga

    @sga.setter
    def sga(self, val):
        self._sga = val

    @property
    def nonrecurring_cost(self):
        """Non-recurring costs from period."""
        return self._nonrecurring_cost

    @nonrecurring_cost.setter
    def nonrecurring_cost(self, val):
        self._nonrecurring_cost = val

    @property
    def tax(self):
        """Total taxes from period."""
        return self._tax

    @tax.setter
    def tax(self, val):
        self._tax = val

    @property
    def depreciation(self):
        """Total depreciation from period."""
        return self._depreciation

    @depreciation.setter
    def depreciation(self, val):
        self._depreciation = val

    @property
    def amortization(self):
        """Total amortization from period."""
        return self._amortization

    @amortization.setter
    def amortization(self, val):
        self._amortization = val

    @property
    def da(self):
        """Total depreciation plus amortization from period."""
        return self.amortization + self.depreciation

    @property
    def rd(self):
        """Research and development costs from period."""
        return self._rd

    @rd.setter
    def rd(self, val):
        self._rd = val

    @property
    def interest(self):
        """Interest expense from period."""
        return self._interest

    @interest.setter
    def interest(self, val):
        self._interest = val

    @property
    def start_date(self):
        """Start date of period. Defaults to one year from today."""
        return self._start_date

    @property
    def end_date(self):
        """End date of period. Defaults to today."""
        return self._end_date
