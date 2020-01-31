from abc import abstractmethod
from autodcf.models.base import AbstractDCF


class AbstractAdvancedDCF(AbstractDCF):

    # More complex ratios to use

    @property
    @abstractmethod
    def cogs_to_sales(self):
        pass

    @property
    @abstractmethod
    def sga_to_sales(self):
        pass

    @property
    @abstractmethod
    def depreciation_to_sales(self):
        pass

    @property
    @abstractmethod
    def amortization_to_sales(self):
        pass

    @property
    @abstractmethod
    def capex_to_sales(self):
        pass

    @property
    @abstractmethod
    def change_nwc_to_change_sales(self):
        pass
