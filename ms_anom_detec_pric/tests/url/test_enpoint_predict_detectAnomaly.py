from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import MagicMock
import os

class DetectAnomalyTest(APITestCase):

    def setUp(self):
        csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.csv')
        if not os.path.exists(csv_file_path):
            self.fail(f'El archivo CSV no se encontró en la ruta: {csv_file_path}')
        with open(csv_file_path, 'r') as file:
            csv_file_content = file.read()
        self.csv_file = MagicMock()
        self.csv_file.read.return_value = csv_file_content.encode('utf-8')
        self.bad_csv_file = MagicMock()
        csv_file_content = csv_file_content.replace('ITEM_ID', 'ITEM_IDd')
        self.bad_csv_file.read.return_value = csv_file_content.encode('utf-8')
        url = reverse('cargar_csv')
        response = self.client.post(url, {'archivo_csv': self.csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_anomaly_detection(self):
        data = {
            'item_id': 'MLB4097203966',
            'price': 800.23
        }
        url = reverse('detect_anomaly')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('item_id', response.data)
        self.assertIn('price', response.data)
        self.assertIn('anomaly', response.data)
        self.assertIn('metadata', response.data)
        self.assertIn('status_code', response.data)

    def test_anomaly_detection_exception(self):
        data = {
            'item_id': 'itemIdNotExist',
            'price': 800.23
        }
        url = reverse('detect_anomaly')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('No existe el item_id', response.data['error'])

