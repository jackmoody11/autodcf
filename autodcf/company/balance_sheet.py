import datetime


class BalanceSheet:
    """Balance sheet for specific company at specific point in time.

    Args:
        cash (float): Cash from balance sheet.
        short_term_investments (float): Short term investments from balance sheet.
        net_receivables (float): Net receivables from balance sheet.
        inventory (float): Inventory from balance sheet.
        other_current_assets (float): Other current assets not described by those above.
        ppe (float): Plant, property, and equipment value from balance sheet.
        goodwill (float): Value of goodwill from balance sheet.
        intangible_assets (float): Value of intangible assets.
        other_lt_assets (float): Value of any other long term assets not included in ppe,
            goodwill, and intangible assets.
        accounts_payable (float): Accounts payable from balance sheet.
        accrued_liabilities (float): Accrued liabilities from balance sheet.
        short_term_debt (float): Short term debt from balance sheet.
        current_part_lt_debt (float): Current part long term debt from balance sheet.
        other_current_liabilities (float): Any other current liabilities not covered by accounts payable,
            accrued liabilities, short term debt, or current part long term debt.
        other_lt_liabilities (float): Any long term liabilities that are not deferred or minority interest.
        deferred_lt_liabilities (float): Deferred long term liabilities from balance sheet.
        minority_interest (float): Minority interest from balance sheet.
        date (datetime.datetime): Date balance sheet was released.

    Attributes:
        cash (float): Cash from balance sheet.
        short_term_investments (float): Short term investments from balance sheet.
        net_receivables (float): Net receivables from balance sheet.
        inventory (float): Inventory from balance sheet.
        other_current_assets (float): Other current assets not described by those above.
        ppe (float): Plant, property, and equipment value from balance sheet.
        goodwill (float): Value of goodwill from balance sheet.
        intangible_assets (float): Value of intangible assets.
        other_lt_assets (float): Value of any other long term assets not included in ppe,
            goodwill, and intangible assets.
        accounts_payable (float): Accounts payable from balance sheet.
        accrued_liabilities (float): Accrued liabilities from balance sheet.
        short_term_debt (float): Short term debt from balance sheet.
        current_part_lt_debt (float): Current part long term debt from balance sheet.
        other_current_liabilities (float): Any other current liabilities not covered by accounts payable,
            accrued liabilities, short term debt, or current part long term debt.
        other_lt_liabilities (float): Any long term liabilities that are not deferred or minority interest.
        deferred_lt_liabilities (float): Deferred long term liabilities from balance sheet.
        minority_interest (float): Minority interest from balance sheet.
        date (datetime.datetime): Date balance sheet was released.
        current_asssets (float): Assets easily converted to cash.
        long_term_assets (float): Assets that are not as easily converted to cash.
        current_liabilities (float): Liabilities which are due soon.
        long_term_liabilities (float): Liabilities not due soon.
        assets (float): Sum of current and long term assets.
        liabilities (float): Sum of current and long term liabilities.
        equity (float): Assets minus liabilities (shareholder equity).
        debt_to_equity (float): Ratio of total liabilities to equity.
    """

    def __init__(self,
                 cash,
                 short_term_investments,
                 net_receivables,
                 inventory,
                 other_current_assets,
                 ppe,
                 goodwill,
                 intangible_assets,
                 other_lt_assets,
                 accounts_payable,
                 accrued_liabilities,
                 short_term_debt,
                 current_part_lt_debt,
                 other_current_liabilities,
                 other_lt_liabilities,
                 deferred_lt_liabilities,
                 minority_interest,
                 date=None):
        # Current assets
        self._cash = cash
        self._short_term_investments = short_term_investments
        self._net_receivables = net_receivables
        self._inventory = inventory
        self._other_current_assets = other_current_assets

        # Long term assets
        self._ppe = ppe
        self._goodwill = goodwill
        self._intangible_assets = intangible_assets
        self._other_lt_assets = other_lt_assets

        # Current liabilities
        self._accounts_payable = accounts_payable
        self._accrued_liabilities = accrued_liabilities
        self._short_term_debt = short_term_debt
        self._current_part_lt_debt = current_part_lt_debt
        self._other_current_liabilities = other_current_liabilities

        # Long term liabilities
        self._other_lt_liabilities = other_lt_liabilities
        self._deferred_lt_liabilities = deferred_lt_liabilities
        self._minority_interest = minority_interest
        self._date = date

    @property
    def cash(self):
        return self._cash

    @property
    def short_term_investments(self):
        return self._short_term_investments

    @property
    def net_receivables(self):
        return self._net_receivables

    @property
    def inventory(self):
        return self._inventory

    @property
    def other_current_assets(self):
        return self._other_current_assets

    @property
    def ppe(self):
        return self._ppe

    @property
    def goodwill(self):
        return self._goodwill

    @property
    def intangible_assets(self):
        return self._intangible_assets

    @property
    def other_lt_assets(self):
        return self._other_lt_assets

    @property
    def accounts_payable(self):
        return self._accounts_payable

    @property
    def accrued_liabilities(self):
        return self._accrued_liabilities

    @property
    def short_term_debt(self):
        return self._short_term_debt

    @property
    def current_part_lt_debt(self):
        return self._current_part_lt_debt

    @property
    def other_current_liabilities(self):
        return self._other_current_liabilities

    @property
    def other_lt_liabilities(self):
        return self._other_lt_liabilities

    @property
    def deferred_lt_liabilities(self):
        return self._deferred_lt_liabilities

    @property
    def minority_interest(self):
        return self._minority_interest

    @property
    def current_assets(self):
        return sum((self.cash,
                    self.short_term_investments,
                    self.net_receivables,
                    self.inventory,
                    self.other_current_assets))

    @property
    def long_term_assets(self):
        return sum((self.ppe,
                    self.goodwill,
                    self.intangible_assets,
                    self.other_lt_assets))

    @property
    def assets(self):
        return self.current_assets + self.long_term_assets

    @property
    def current_liabilites(self):
        return sum((self.accounts_payable,
                    self.accrued_liabilities,
                    self.short_term_debt,
                    self.current_part_lt_debt,
                    self.other_current_liabilities))

    @property
    def long_term_liabilities(self):
        return sum((self.other_lt_liabilities,
                    self.deferred_lt_liabilities,
                    self.minority_interest))

    @property
    def liabilities(self):
        return self.current_liabilites + self.long_term_liabilities

    @property
    def equity(self):
        return self.assets - self.liabilities

    @property
    def debt_to_equity(self):
        """float: Ratio of total liabilities to shareholder equity."""
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
