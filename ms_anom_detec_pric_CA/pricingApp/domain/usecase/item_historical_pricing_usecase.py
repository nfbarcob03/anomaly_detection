from ast import List
from csv import DictReader
from pricingApp.domain.model import ItemHistoricalPricing
from pricingApp.domain.model import AbstractItemHistoricalPricingRepository
from .abstract_item_historical_pricing_usecase import AbstractItemHistoricalPricingUseCase

class ItemHistoricalPricingUseCase(AbstractItemHistoricalPricingUseCase):
    def __init__(self, itemHistoricalPricingRepository:AbstractItemHistoricalPricingRepository):
        self.repo = itemHistoricalPricingRepository
    
    def cargarHistoricalData(self,reader:DictReader):
        try:
            for fila in reader:
                self.repo.insert(itemId=fila['ITEM_ID'], 
                                                        ordCloseDt=fila['ORD_CLOSED_DT'], 
                                                        price=fila['PRICE']) 
            number_records_saved = str(reader.line_num-1) 
            print('LogInfo: Carga exitosa del archivo plano con ' + number_records_saved + ' registros cargados') 
            return True, number_records_saved
        except Exception as e:
             print('LogError:' + repr(e))
             return False, '0'
    
    def consultarPreciosByIdItem(self, idItem:str):
        return self.repo.getByItemId(itemId=idItem)