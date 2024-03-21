from ast import List
from csv import DictReader
from pricingApp.domain.model import AnomalyDetectionModelInput,AnomalyDetectionModelOutput
from pricingApp.domain.model import AbstractItemHistoricalPricingRepository, AbstractAnomalyDetectionModelRepository
from .gateway.abstract_anomaly_detection_model_usecase import AbstractAnomalyDetectionModelUseCase

class AnomalyDetectionModelUseCase(AbstractAnomalyDetectionModelUseCase):
    def __init__(self, anomalyDetectionModelRepository:AbstractAnomalyDetectionModelRepository,
                 itemHistoricalPricingRepository:AbstractItemHistoricalPricingRepository):
        self.repoModel = anomalyDetectionModelRepository
        self.repoItem = itemHistoricalPricingRepository
    
    def isAnomay(self,input:AnomalyDetectionModelInput):
        historical_prices = self.repoItem.getByItemId(input.item_id)
        if not historical_prices:
            print('LogError: No existe el item_id = {0} en el historico de precios'.format(input.item_id))
            raise Exception('No existe el item_id = {0} en el historico de precios'.format(input.item_id))
        ##historical_prices = [item.model_dump() for item in historical_prices]
        listAnomalyDetectonModelInput = [AnomalyDetectionModelInput(item_id = x.item_id,price = x.price) for x in historical_prices]
        listAnomalyDetectonModelInput.append(input)
        predict = self.repoModel.getPredict(listAnomalyDetectonModelInput)
        # Determinar si el último precio es una anomalía
        is_anomaly = (predict[-1] == -1)  # -1 indica una anomalía
        return AnomalyDetectionModelOutput(item_id = input.item_id, price = input.price, anomaly= is_anomaly, metadata={},
                              status_code =200)
    

