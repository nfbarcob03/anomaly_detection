import pytest
from pydantic import ValidationError

from ..anomaly_detection_model import AnomalyDetectionModelOutput

def test_customer_create():
    anomalyDetectionModelOutput = AnomalyDetectionModelOutput(
        item_id = 'item_id'
        price = 10.10
        anomaly = True
        metadata = {}
        status_code = 200
    )

    assert anomalyDetectionModelOutput
    assert anomalyDetectionModelOutput.item_id == "item_id"
    assert anomalyDetectionModelOutput.price == 10.10
    assert anomalyDetectionModelOutput.anomaly == True
    assert anomalyDetectionModelOutput.metadata == {}
    assert anomalyDetectionModelOutput.status_code == 200

