import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pricingApp.domain.usecase import ItemHistoricalPricingUseCase
from pricingApp.driven_adapter.orm_driver import ItemHistoricalRepositoryAdapter 

class CargarCSV(APIView):
    def post(self, request):
        if 'archivo_csv' not in request.FILES:
            return Response({'error': 'Se requiere un archivo CSV'}, status=status.HTTP_400_BAD_REQUEST)
        archivo_csv = request.FILES['archivo_csv']
        decoded_file = archivo_csv.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        repo = ItemHistoricalRepositoryAdapter()
        use_case = ItemHistoricalPricingUseCase(repo)
        result, number_records_saved = use_case.cargarHistoricalData(reader)
        if result:
            return Response({'mensaje': number_records_saved + ' Datos insertados correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Problemas al cargar el archivo plano. verificar y reintentar de nuevo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            