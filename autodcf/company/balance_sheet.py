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
        other_lt_assets (float): Value of any other long-term assets not included in ppe,
            goodwill, and intangible assets.
        accounts_payable (float): Accounts payable from balance sheet.
        accrued_liabilities (float): Accrued liabilities from balance sheet.
        short_term_debt (float): Short term debt from balance sheet.
        current_part_lt_debt (float): Current part long-term debt from balance sheet.
        other_current_liabilities (float): Any other current liabilities not covered by accounts payable,
            accrued liabilities, short term debt, or current part long-term debt.
        long_term_debt (float): long-term debt.
        other_lt_liabilities (float): Any long-term liabilities that are not deferred or minority interest.
        deferred_lt_liabilities (float): Deferred long-term liabilities from balance sheet.
        minority_interest (float): Minority interest from balance sheet.
        date (datetime.datetime, optional): Date balance sheet was released.
        other_lt_liability_debt_multiplier (float, optional): Long-term liabilities that are long-term debt.
            Should be between 0 and 1 inclusive. Defaults to 0.
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
                 long_term_debt,
                 other_current_liabilities,
                 other_lt_liabilities,
                 deferred_lt_liabilities,
                 minority_interest,
                 date=None,
                 other_lt_liability_debt_multiplier=0):
        # Current assets
        self._cash = cash
        self._short_term_investments = short_term_investments
        self._net_receivables = net_receivables
        self._inventory = inventory
        self._other_current_assets = other_current_assets

        # long-term assets
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

        # long-term liabilities
        self._long_term_debt = long_term_debt
        self._other_lt_liabilities = other_lt_liabilities
        self._deferred_lt_liabilities = deferred_lt_liabilities
        self._minority_interest = minority_interest

        # Options
        self._other_lt_liability_debt_multiplier = other_lt_liability_debt_multiplier
        self._date = date

    @property
    def cash(self):
        """Cash available at date of filing."""
        return self._cash

    @property
    def short_term_investments(self):
        """Short term investments at date of filing."""
        return self._short_term_investments

    @property
    def net_receivables(self):
        """Net receivables at date of filing."""
        return self._net_receivables

    @property
    def inventory(self):
        """Value of inventory at date of filing."""
        return self._inventory

    @property
    def other_current_assets(self):
        """Other current assets not included in cash, short term investments, net receivables, and inventory."""
        return self._other_current_assets

    @property
    def ppe(self):
        """Value of plant, property, and equipment at date of filing."""
        return self._ppe

    @property
    def goodwill(self):
        """Value of goodwill at date of filing."""
        return self._goodwill

    @property
    def intangible_assets(self):
        """Value of intangible assets at date of filing."""
        return self._intangible_assets

    @property
    def other_lt_assets(self):
        """Other long-term assets not included in PPE, goodwill, and intangible assets."""
        return self._other_lt_assets

    @property
    def accounts_payable(self):
        """Amount of accounts payable at date of filing."""
        return self._accounts_payable

    @property
    def accrued_liabilities(self):
        """Amount of accrued liabilities at date of filing."""
        return self._accrued_liabilities

    @property
    def short_term_debt(self):
        """Amount of short term debt at date of filing."""
        return self._short_term_debt

    @property
    def current_part_lt_debt(self):
        """Amount of long-term debt that is due soon at date of filing."""
        return self._current_part_lt_debt

    @property
    def other_current_liabilities(self):
        """Other current liabilities.

        All other current liabilities not included in accounts payable, accrued liabilities, short term debt,
        and current part long-term debt.
        """
        return self._other_current_liabilities

    @property
    def long_term_debt(self):
        """Amount of long-term debt not due currently at date of filing."""
        return self._long_term_debt

    @property
    def deferred_lt_liabilities(self):
        """Deferred long-term liabilities at date of filing."""
        return self._deferred_lt_liabilities

    @property
    def minority_interest(self):
        """Minority interest at date of filing."""
        return self._minority_interest

    @property
    def other_lt_liabilities(self):
        """Other long-term liabilities.

        All other long-term liabilities not included in long-term debt, deferred long-term liabilities and
        minority interest."""
        return self._other_lt_liabilities

    @property
    def current_assets(self):
        """Total value of current assets at date of filing."""
        return sum((self.cash,
                    self.short_term_investments,
                    self.net_receivables,
                    self.inventory,
                    self.other_current_assets))

    @property
    def long_term_assets(self):
        """Total value of long-term assets at date of filing."""
        return sum((self.ppe,
                    self.goodwill,
                    self.intangible_assets,
                    self.other_lt_assets))

    @property
    def assets(self):
        """Total value of assets at date of filing."""
        return self.current_assets + self.long_term_assets

    @property
    def current_liabilites(self):
        """Total amount of current liabilities at date of filing."""
        return sum((self.accounts_payable,
                    self.accrued_liabilities,
                    self.short_term_debt,
                    self.current_part_lt_debt,
                    self.other_current_liabilities))

    @property
    def long_term_liabilities(self):
        """Total amount of long-term liabilities at date of filing."""
        return sum((self.other_lt_liabilities,
                    self.long_term_debt,
                    self.deferred_lt_liabilities,
                    self.minority_interest))

    @property
    def liabilities(self):
        """Total amount of liabilities at date of filing."""
        return self.current_liabilites + self.long_term_liabilities

    @property
    def net_debt(self):
        """Net debt (derived from short and long-term debt minus cash-like assets)."""
        return (self.short_term_debt + self.long_term_debt
                + self.other_lt_liabilities * self.other_lt_liability_debt_multiplier  # noqa: W503
                - self.cash - self.short_term_investments)  # noqa: W503

    @property
    def equity(self):
        """Total assets minus total liabilities at date of filing."""
        return self.assets - self.liabilities

    @property
    def debt_to_equity(self):
        """float: Ratio of total liabilities to shareholder equity."""
        return self.liabilities / self.equity

    @property
    def date(self):
        """Date of filing."""
        return self._date

    @date.setter
    def date(self, val):
        if isinstance(val, datetime.datetime):
            self._date = val
        else:
            raise TypeError

    @property
    def other_lt_liability_debt_multiplier(self):
        return self._other_lt_liability_debt_multiplier
