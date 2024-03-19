from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pricingApp.model import ItemHistoricalPricing
from pricingApp.serializer import HistoricalPricingSerializer

class HistoricalPricingListView(generics.ListAPIView):
    serializer_class = HistoricalPricingSerializer
    
    def get_queryset(self):
        # Obtenemos el parámetro item_id de la URL
        item_id = self.kwargs['item_id']
        # Filtramos los registros que tengan el mismo item_id
        queryset = ItemHistoricalPricing.objects.filter(item_id=item_id)
        return queryset