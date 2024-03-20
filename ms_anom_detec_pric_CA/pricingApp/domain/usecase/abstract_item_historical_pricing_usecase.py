from abc import ABC, abstractmethod
from csv import DictReader

class AbstractItemHistoricalPricingUseCase(ABC):
    @abstractmethod
    def cargarHistoricalData(self,reader:DictReader):
        ...

    @abstractmethod
    def consultarPreciosByIdItem(self, idItem:str):
        ...
