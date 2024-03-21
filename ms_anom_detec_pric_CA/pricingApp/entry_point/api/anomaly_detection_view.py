from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pricingApp.domain.model import AnomalyDetectionModelInput, AnomalyDetectionModelOutput

from pricingApp.domain.usecase import AnomalyDetectionModelUseCase
from pricingApp.driven_adapter.orm_driver import ItemHistoricalRepositoryAdapter
from pricingApp.driven_adapter.anomaly_model import AnomalyDetectionRepositoryAdapter

class DetectAnomaly(APIView):
    def post(self, request):
        try:
            # Obtener el precio y el ID del artículo del cuerpo de la solicitud POST
            inputAnomalyDetectionModel = AnomalyDetectionModelInput(item_id=request.data.get('item_id'),
                                                                    price = float(request.data.get('price')))
            repoItem = ItemHistoricalRepositoryAdapter()
            repoModel = AnomalyDetectionRepositoryAdapter()
            use_case = AnomalyDetectionModelUseCase(anomalyDetectionModelRepository =repoModel, 
                                                    itemHistoricalPricingRepository = repoItem )
            anomalyDetectionModelOutput = use_case.isAnomay(inputAnomalyDetectionModel)
            return Response(anomalyDetectionModelOutput.model_dump(), status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)