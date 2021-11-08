from datetime import timezone
from django.db import models


class ChartModel(models.Model):
    Product_id = models.BigIntegerField()
    datefrom = models.DateTimeField()
    dateto = models.DateTimeField()

    def __init__(self, pro_id, dfrom, dto):
        self.Product_id = pro_id
        self.datefrom = dfrom
        self.dateto = dto


class ChartResponseModel(models.Model):
    quantity = models.IntegerField()
    price = models.IntegerField()
    Customer_bidprice = models.IntegerField()
    datefrom = models.DateTimeField()

    def __init__(self, qn, pr, df,cb):
        self.quantity = qn
        self.datefrom = df
        self.price = pr
        self.Customer_bidprice = cb

    def __str__(self):
        return str(self.datefrom)
