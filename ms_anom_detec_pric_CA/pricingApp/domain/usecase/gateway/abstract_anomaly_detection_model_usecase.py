from abc import ABC, abstractmethod
from pricingApp.domain.model import AnomalyDetectionModelInput


class AbstractAnomalyDetectionModelUseCase(ABC):
    @abstractmethod
    def isAnomay(self,anomalyDetectionModelInput:AnomalyDetectionModelInput):
        ...
