from django.db import models
import ms_anomaly_detection_pricing.settings as settings 
class ItemHistoricalPricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_id = models.CharField(max_length=250, blank=True, null=True)
    ord_closed_dt = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'item_historical_pricing' 
        