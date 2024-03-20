from abc import ABC, abstractmethod
from ..historical_pricing import ItemHistoricalPricing
from typing import Optional, Sequence
class AbstractItemHistoricalPricingRepository(ABC):
    @abstractmethod
    def insert(self,itemId, ordCloseDt, price) -> Optional[ItemHistoricalPricing]:
        ...
    
    @abstractmethod
    def getByItemId(self, itemId) -> Optional[Sequence[ItemHistoricalPricing]]:
        ...