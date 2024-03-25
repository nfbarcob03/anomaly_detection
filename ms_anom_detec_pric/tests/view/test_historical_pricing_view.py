from django.test import TestCase
from pricingApp.model import ItemHistoricalPricing
from pricingApp.view import HistoricalPricingListView, DetectAnomaly, CargarCSV
from pricingApp.serializer import HistoricalPricingSerializer

class HistoricalPricingListViewTest(TestCase):
    historicalPricingListView: HistoricalPricingListView
    historicalPricingSerializer: HistoricalPricingSerializer
    itemHistoricalPricing: ItemHistoricalPricing
    listItem =[]

    def setUp(self):
        self.itemHistoricalPricing = ItemHistoricalPricing.objects.create(id =1, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23)
        self.listItem.append(self.itemHistoricalPricing)
        self.listItem.append(ItemHistoricalPricing.objects.create(id =2, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
        self.listItem.append(ItemHistoricalPricing.objects.create(id =3, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
        self.historicalPricingSerializer = HistoricalPricingSerializer()
        self.historicalPricingListView = HistoricalPricingListView(kwargs={'item_id':'ItemId'})
    
    def test_get_historical_pricing_by_id_item(self):

        queryset = self.historicalPricingListView.get_queryset()

        self.assertEqual(len(self.listItem), len(queryset))
        self.assertEqual(self.listItem[0].item_id, queryset[0].item_id)
