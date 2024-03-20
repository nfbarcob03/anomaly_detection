from django.db import models
class ItemHistoricalPricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.CharField(max_length=250, blank=True, null=True)
    ord_closed_dt = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_historical_pricing'
        