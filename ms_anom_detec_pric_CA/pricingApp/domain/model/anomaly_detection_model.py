import datetime
from pydantic import BaseModel
class AnomalyDetectionModelOutput(BaseModel):
    item_id : str
    price: float
    anomaly : bool
    metadata : dict
    status_code: int

class AnomalyDetectionModelInput(BaseModel):
    item_id : str
    price: float