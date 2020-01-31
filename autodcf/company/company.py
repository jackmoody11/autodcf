from autodcf.company import BalanceSheet, CashFlows, IncomeStatement


class Company:
    """Encapsulates info about company's financial standing to be used in models."""

    def __init__(self,
                 fully_diluted_shares,
                 price_per_share,
                 balance_sheet,
                 cash_flows,
                 income_statement):
        self._fully_diluted_shares = fully_diluted_shares
        self._price_per_share = price_per_share
        self._balance_sheet = balance_sheet
        self._cash_flows = cash_flows
        self._income_statement = income_statement

    @property
    def fully_diluted_shares(self):
        return self._fully_diluted_shares

    @fully_diluted_shares.setter
    def fully_diluted_shares(self, val):
        self._fully_diluted_shares = val

    @property
    def price_per_share(self):
        return self._price_per_share

    @price_per_share.setter
    def price_per_share(self, val):
        self._price_per_share = val

    @property
    def balance_sheet(self):
        return self._balance_sheet

    @balance_sheet.setter
    def balance_sheet(self, val):
        if isinstance(val, BalanceSheet):
            self._balance_sheet = val
        else:
            raise TypeError

    @property
    def cash_flows(self):
        return self._cash_flows

    @cash_flows.setter
    def cash_flows(self, val):
        if isinstance(val, CashFlows):
            self._cash_flows = val
        else:
            raise TypeError

    @property
    def income_statement(self):
        return self._income_statement

    @income_statement.setter
    def income_statement(self, val):
        if isinstance(val, IncomeStatement):
            self._income_statement = val
        else:
            raise TypeError
