import datetime
from pydantic import BaseModel
class ItemHistoricalPricing(BaseModel):
    item_id : str
    ord_closed_dt : datetime.date
    price : float
    