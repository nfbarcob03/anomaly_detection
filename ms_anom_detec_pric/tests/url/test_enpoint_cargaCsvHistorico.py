from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import MagicMock
import os

class CargaCsvEnpointTest(APITestCase):

    csv_file:MagicMock
    bad_csv_file: MagicMock
    

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
        


    def test_cargar_csv_desde_archivo(self):
        url = reverse('cargar_csv')
        response = self.client.post(url, {'archivo_csv': self.csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(response.data['mensaje'], 'Datos insertados correctamente')

    
    def test_cargar_csv_desde_archivo_exception(self):
        url = reverse('cargar_csv')
        response = self.client.post(url, {'archivo_csv': self.bad_csv_file}, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn('Error procesando el archivo .csv', response.data['error'])
    
    def test_cargar_csv_desde_archivo_not_file(self):
        url = reverse('cargar_csv')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['error'], 'Se requiere un archivo CSV')