class CashFlows:
    """Statement of Cash Flows object for specific company during a specific time period.

    Args:
        capex (Union[int, float]): Capital expenditures for cash flow period.

    Attributes:
        capex (Union[int, float]): Capital expenditures for cash flow period.
    """

    def __init__(self,
                 capex):
        self._capex = capex

    @property
    def capex(self):
        return self._capex

    @capex.setter
    def capex(self, val):
        self._capex = val
