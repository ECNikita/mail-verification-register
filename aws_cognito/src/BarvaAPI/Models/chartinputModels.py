from django.db import models


class ChartModel(models.Model):
    Product_id = models.BigIntegerField()
    datefrom = models.DateTimeField()
    dateto = models.DateTimeField()

    def __init__(self , pro_id,dfrom,dto):
        self.Product_id = pro_id
        self.datefrom =dfrom
        self.dateto = dto

class ChartResponseModel(models.Model):
    price = models.IntegerField()
    quantity =models.IntegerField()
    datefrom = models.DateTimeField()

    def __init__(self,pr,qn,df):
        self.price = pr
        self.quantity =qn
        self.datefrom =df
