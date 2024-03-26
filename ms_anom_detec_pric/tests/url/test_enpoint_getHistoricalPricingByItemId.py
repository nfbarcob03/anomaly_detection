from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from pricingApp.model import ItemHistoricalPricing
from rest_framework.test import APIClient

class HistoricalPricingByItemIdEndpointTest(TestCase):
    url : str
    client: APIClient
    itemHistoricalPricingExample: ItemHistoricalPricing
    listItem=[]


    def setUp(self):
        self.item_id = 'ItemId'
        self.url = reverse('historical_pricing_list', kwargs={'item_id': self.item_id})
        self.client = APIClient()

        ##Siembra de obetos en la base de datos para que el servicio encuentre data
        self.itemHistoricalPricing = ItemHistoricalPricing.objects.create(id =1, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23)
        self.listItem.append(self.itemHistoricalPricing)
        self.listItem.append(ItemHistoricalPricing.objects.create(id =2, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
        self.listItem.append(ItemHistoricalPricing.objects.create(id =3, item_id='ItemId', 
                                                      ord_closed_dt='2024-03-03', price=800.23))
    
    def test_historical_pricing_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
         # Verificar que el contenido de la respuesta sea una lista
        self.assertIsInstance(response.data, list)

        # Verificar que la longitud de la respuesta sea igual a la longitud de self.listItem
        self.assertEqual(len(response.data), len(self.listItem))

    