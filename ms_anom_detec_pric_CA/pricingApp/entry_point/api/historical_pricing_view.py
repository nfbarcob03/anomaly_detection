
from rest_framework.views import APIView
from rest_framework import status
from pricingApp.driven_adapter.orm_driver import ItemHistoricalRepositoryAdapter
from .historical_pricing_item_serializer import HistoricalPricingSerializer
from pricingApp.domain.usecase import ItemHistoricalPricingUseCase
from rest_framework.response import Response

class HistoricalPricingListView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtenemos el parámetro item_id de la URL
        idItem = kwargs['item_id']
        repo = ItemHistoricalRepositoryAdapter()
        use_case = ItemHistoricalPricingUseCase(repo)
        listEntity = use_case.consultarPreciosByIdItem(idItem=idItem)
        return Response([repr(item) for item in listEntity], status=status.HTTP_200_OK)
