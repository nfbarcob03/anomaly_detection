from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pricingApp.model import ItemHistoricalPricing
from sklearn.ensemble import IsolationForest
from hampel import hampel
import pandas as pd

class DetectAnomaly(APIView):
    def post(self, request):
        try:
            # Obtener el precio y el ID del artículo del cuerpo de la solicitud POST
            price = float(request.data.get('price'))
            item_id = request.data.get('item_id')
            
            # Obtener el histórico de precios del artículo de la base de datos
            historical_prices = ItemHistoricalPricing.objects.filter(item_id=item_id).order_by('ord_closed_dt')

            if not historical_prices:
                return Response({'error': 'No existe el item_id en el historico de precios'}, status=status.HTTP_404_NOT_FOUND)

            prices = pd.Series([float(entry.price) for entry in historical_prices])
            
            # Agregar el nuevo precio al histórico
            prices = pd.concat([prices,pd.Series([price])])
            
            # Convertir los precios a un formato adecuado para el modelo Isolation Forest
            X = prices.values.reshape(-1, 1)
            
            # Entrenar el modelo Isolation Forest
            isolation_forest = IsolationForest(contamination='auto', random_state=42)
            isolation_forest.fit(X)
            
            # Predecir las anomalías
            predictions = isolation_forest.predict(X)
            
            # Determinar si el último precio es una anomalía
            is_anomaly = (predictions[-1] == -1)  # -1 indica una anomalía
            
            # Devolver una respuesta con el resultado
            return Response({'is_anomaly': is_anomaly}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)