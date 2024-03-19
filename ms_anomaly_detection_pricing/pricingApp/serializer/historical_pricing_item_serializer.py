from pricingApp.model import ItemHistoricalPricing
from rest_framework import serializers
class HistoricalPricingSerializer(serializers.ModelSerializer):
 class Meta:
   model = ItemHistoricalPricing
   fields = ['item_id', 'ord_closed_dt', 'price']