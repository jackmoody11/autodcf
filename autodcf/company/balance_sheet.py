class BalanceSheet:
    """Balance sheet for specific company at specific point in time. """

    def __init__(self,
                 assets,
                 liabilities):
        self._assets = assets
        self._liabilities = liabilities

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
