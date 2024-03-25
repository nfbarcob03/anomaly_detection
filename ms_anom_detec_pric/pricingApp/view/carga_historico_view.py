import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pricingApp.model import ItemHistoricalPricing 

class CargarCSV(APIView):
    def post(self, request):
        if 'archivo_csv' not in request.FILES:
            return Response({'error': 'Se requiere un archivo CSV'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            archivo_csv = request.FILES['archivo_csv']
            decoded_file = archivo_csv.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for fila in reader:
                ItemHistoricalPricing.objects.create(item_id=fila['ITEM_ID'], 
                                                     ord_closed_dt=fila['ORD_CLOSED_DT'], 
                                                     price=fila['PRICE'])  
            return Response({'mensaje': 'Datos insertados correctamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return Response({'error': 'Error procesando el archivo .csv, ver los logs para mas informacion'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)