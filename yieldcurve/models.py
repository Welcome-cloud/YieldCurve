from django.db import models

class YieldCurve(models.Model):
    date = models.DateField()
    maturity = models.CharField(max_length=20)
    yield_value = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.maturity} - {self.yield_value}"

# Create your models here.