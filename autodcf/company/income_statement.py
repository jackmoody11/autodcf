class IncomeStatement:
    """Income statement object for specific company during a specific time period. """

    def __init__(self,
                 sales,
                 cogs,
                 sga,
                 rd,
                 depreciation,
                 amortization,
                 nonrecurring_cost,
                 interest,
                 tax):
        self._sales = sales
        self._cogs = cogs
        self._sga = sga
        self._rd = rd
        self._nonrecurring_cost = nonrecurring_cost
        self._interest = interest
        self._tax = tax
        self._depreciation = depreciation
        self._amortization = amortization

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, val):
        self._sales = val

    @property
    def cogs(self):
        return self._cogs

    @cogs.setter
    def cogs(self, val):
        self._cogs = val

    @property
    def sga(self):
        return self._sga

    @sga.setter
    def sga(self, val):
        self._sga = val

    @property
    def nonrecurring_cost(self):
        return self._nonrecurring_cost

    @nonrecurring_cost.setter
    def nonrecurring_cost(self, val):
        self._nonrecurring_cost = val

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, val):
        self._tax = val

    @property
    def depreciation(self):
        return self._depreciation

    @depreciation.setter
    def depreciation(self, val):
        self._depreciation = val

    @property
    def amortization(self):
        return self._amortization

    @amortization.setter
    def amortization(self, val):
        self._amortization = val

    @property
    def rd(self):
        return self._rd

    @rd.setter
    def rd(self, val):
        self._rd = val

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, val):
        self._interest = val
