from ast import List
from typing import Optional, Sequence

from sklearn.ensemble import IsolationForest
from pricingApp.domain.model import AbstractAnomalyDetectionModelRepository
from pricingApp.domain.model import AnomalyDetectionModelOutput,AnomalyDetectionModelInput
import pandas as pd

class AnomalyDetectionRepositoryAdapter(AbstractAnomalyDetectionModelRepository):

    
    def getPredict(self,anomaliDetectionListInput:Sequence[AnomalyDetectionModelInput]):
        prices = pd.Series([float(entry.price) for entry in anomaliDetectionListInput])
        
        # Convertir los precios a un formato adecuado para el modelo Isolation Forest
        X = prices.values.reshape(-1, 1)
        
        # Entrenar el modelo Isolation Forest
        isolation_forest = IsolationForest(contamination='auto', random_state=42)
        isolation_forest.fit(X)
        
        # Predecir las anomalías
        predictions = isolation_forest.predict(X)
        
        return predictions