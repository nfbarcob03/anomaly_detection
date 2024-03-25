from django.test import TestCase
from pricingApp.model import ItemHistoricalPricing

class ItemHistoricalPricingTest(TestCase):
    itemHistoricalPricing: ItemHistoricalPricing
    listItem =[]

    def setUp(self):

        self.itemHistoricalPricing = ItemHistoricalPricing.objects.create(id =1, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23)
        self.listItem.append(self.itemHistoricalPricing)
        self.listItem.append(ItemHistoricalPricing.objects.create(id =2, item_id='ItemId2', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
        self.listItem.append(ItemHistoricalPricing.objects.create(id =3, item_id='ItemId3', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
    
    def test_item_historical_pricing(self):
        testObject = ItemHistoricalPricing.objects.get(id=1)
        self.assertEquals(self.itemHistoricalPricing.item_id, testObject.item_id)
        self.assertEquals(self.itemHistoricalPricing.id, testObject.id)
        self.assertEquals(self.itemHistoricalPricing.price, testObject.price)
        self.assertEquals(len(ItemHistoricalPricing.objects.all()), len(self.listItem))
