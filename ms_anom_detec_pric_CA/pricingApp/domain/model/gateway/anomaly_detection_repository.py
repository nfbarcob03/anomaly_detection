from abc import ABC, abstractmethod
from ..anomaly_detection_model import AnomalyDetectionModelInput
from typing import Optional, Sequence
class AbstractAnomalyDetectionModelRepository(ABC):
    @abstractmethod
    def getPredict(self,anomaliDetectionListInput:Sequence[AnomalyDetectionModelInput]) -> Optional[Sequence[int]]:
        ...
    