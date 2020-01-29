import datetime


class BalanceSheet:
    """Balance sheet for specific company at specific point in time. """

    def __init__(self,
                 assets,
                 liabilities,
                 date=None):
        self._assets = assets
        self._liabilities = liabilities
        self._date = date

    @property
    def assets(self):
        return self._assets

    @assets.setter
    def assets(self, val):
        self._assets = val

    @property
    def liabilities(self):
        return self._liabilities

    @liabilities.setter
    def liabilities(self, val):
        self._liabilities = val

    @property
    def equity(self):
        return self.assets - self.liabilities

    @property
    def debt_to_equity(self):
        return self.liabilities / self.equity

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        if isinstance(val, datetime.datetime):
            self._date = val
        else:
            raise TypeError
