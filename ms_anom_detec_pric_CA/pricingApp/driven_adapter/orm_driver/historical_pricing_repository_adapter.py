from typing import Optional, Sequence
from pricingApp.domain.model import AbstractItemHistoricalPricingRepository
from pricingApp.domain.model import ItemHistoricalPricing
from .model.historical_pricing_data import ItemHistoricalPricingData


class ItemHistoricalRepositoryAdapter(AbstractItemHistoricalPricingRepository):

    def insert(self, itemId, ordCloseDt, price) -> ItemHistoricalPricing:
        itemHistorical = ItemHistoricalPricingData.objects.create(item_id = itemId, ord_closed_dt = ordCloseDt, price = price)  
        return ItemHistoricalPricing(**itemHistorical.__dict__)

    def getByItemId(self, itemId) -> Optional[Sequence[ItemHistoricalPricing]]:
        listData = ItemHistoricalPricingData.objects.filter(item_id=itemId).order_by('ord_closed_dt')
        return  [
            ItemHistoricalPricing(
                item_id=item.item_id,
                ord_closed_dt=item.ord_closed_dt,
                price=item.price
                )
                for item in listData
                ]
        
        