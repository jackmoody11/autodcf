from autodcf.company import BalanceSheet, CashFlows, IncomeStatement


class Company:
    """Encapsulates info about company's financial standing to be used in models."""

    def __init__(self,
                 fully_diluted_shares_outstanding,
                 price_per_share,
                 balance_sheet,
                 cash_flows,
                 income_statement):
        self.fully_diluted_shares_outstanding = fully_diluted_shares_outstanding
        self.price_per_share = price_per_share
        self.balance_sheet = balance_sheet
        self.cash_flows = cash_flows
        self.income_statement = income_statement

    @property
    def fully_diluted_shares_outstanding(self):
        return self.fully_diluted_shares_outstanding

    @fully_diluted_shares_outstanding.setter
    def fully_diluted_shares_outstanding(self, val):
        self.fully_diluted_shares_outstanding = val

    @property
    def price_per_share(self):
        return self.price_per_share

    @price_per_share.setter
    def price_per_share(self, val):
        self.price_per_share = val

    @property
    def balance_sheet(self):
        return self.balance_sheet

    @balance_sheet.setter
    def balance_sheet(self, val):
        if isinstance(val, BalanceSheet):
            self.balance_sheet = val
        else:
            raise TypeError

    @property
    def cash_flows(self):
        return self.cash_flows

    @cash_flows.setter
    def cash_flows(self, val):
        if isinstance(val, CashFlows):
            self.cash_flows = val
        else:
            raise TypeError

    @property
    def income_statement(self):
        return self.income_statement

    @income_statement.setter
    def income_statement(self, val):
        if isinstance(val, IncomeStatement):
            self.income_statement = val
        else:
            raise TypeError
