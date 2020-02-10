from abc import ABC, abstractmethod


class AbstractDCF(ABC):
    """Abstract base class for all DCF models."""

    # Basic assumptions

    @property
    @abstractmethod
    def company(self):
        pass

    @property
    @abstractmethod
    def sales_growth(self):
        pass

    @property
    @abstractmethod
    def discount_rate(self):
        pass

    @property
    @abstractmethod
    def terminal_growth_rate(self):
        pass

    @property
    @abstractmethod
    def window(self):
        pass
