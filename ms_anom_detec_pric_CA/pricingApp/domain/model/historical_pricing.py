import datetime
from pydantic import BaseModel
class ItemHistoricalPricing(BaseModel):
    item_id : str
    ord_closed_dt : datetime.date
    price : float
    
    def __repr__(self):
        return f"{self.item_id} - {self.price} - {self.ord_closed_dt}"
    
    def __str__(self):
        return f"{self.item_id} - {self.price} - {self.ord_closed_dt}"