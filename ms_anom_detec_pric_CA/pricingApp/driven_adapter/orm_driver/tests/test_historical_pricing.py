from django.test import TestCase
from pricingApp.driven_adapter.orm_driver import ItemHistoricalPricingData# Importa desde el mismo paquete
from datetime import date

class ItemHistoricalPricingTestCase(TestCase):
    def setUp(self):
        self.item = ItemHistoricalPricingData.objects.create(
            item_id='MLB1234567890',
            ord_closed_dt=date.today(),
            price=99.99
        )

    def test_item_creation(self):
        """Test that a new ItemHistoricalPricing instance is created correctly."""
        self.assertEqual(self.item.item_id, 'MLB1234567890')
        self.assertEqual(self.item.ord_closed_dt, date.today())
        self.assertEqual(self.item.price, 99.99)

    def test_blank_fields(self):
        """Test that blank fields are allowed."""
        blank_item = ItemHistoricalPricingData.objects.create()
        self.assertIsNone(blank_item.item_id)
        self.assertIsNone(blank_item.ord_closed_dt)
        self.assertIsNone(blank_item.price)

    def test_null_fields(self):
        """Test that null fields are allowed."""
        null_item = ItemHistoricalPricingData.objects.create(
            item_id=None,
            ord_closed_dt=None,
            price=None
        )
        self.assertIsNone(null_item.item_id)
        self.assertIsNone(null_item.ord_closed_dt)
        self.assertIsNone(null_item.price)