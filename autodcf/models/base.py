import pandas as pd
from abc import ABC, abstractmethod


class AbstractDCF(ABC):
    """Abstract base class for DCF models. """

    def __init__(self):
        pass

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
