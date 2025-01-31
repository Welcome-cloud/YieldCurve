from django.db import models

class YieldCurve(models.Model):
    date = models.DateField()
    ytm_1d = models.FloatField(null=True, blank=True)
    ytm_7d = models.FloatField(null=True, blank=True)
    ytm_14d = models.FloatField(null=True, blank=True)
    ytm_28d = models.FloatField(null=True, blank=True)
    ytm_91d = models.FloatField(null=True, blank=True)
    ytm_182d = models.FloatField(null=True, blank=True)
    ytm_12m = models.FloatField(null=True, blank=True)
    ytm_2y = models.FloatField(null=True, blank=True)
    ytm_3y = models.FloatField(null=True, blank=True)
    ytm_5y = models.FloatField(null=True, blank=True)
    ytm_7y = models.FloatField(null=True, blank=True)
    ytm_10y = models.FloatField(null=True, blank=True)


    #maturity = models.CharField(max_length=12)
    #yield_value = models.FloatField()

    def __str__(self):
        return f"{self.date}"

# Create your models here.