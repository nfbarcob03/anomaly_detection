import pytest
from pricingApp.driven_adapter.orm_driver import ItemHistoricalPricingData
from datetime import date

def testItemHistoricalPricingData_creation():
    historical_pricing =  ItemHistoricalPricingData.objects.create(
        item_id='MLB1234567890',
        ord_closed_dt=date.today(),
        price=99.99
    )
    assert historical_pricing.item_id == 'MLB1234567890'
    assert historical_pricing.ord_closed_dt == date.today()
    assert historical_pricing.price == 99.99