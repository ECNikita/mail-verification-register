from django.db import models


class Product_pricebyproducerModel(models.Model):
    Product_id = models.BigIntegerField(blank=True, null=True)
    Producer_id = models.BigIntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    datefrom = models.DateTimeField()
    dateto = models.DateTimeField()
    Lotunit_id = models.BigIntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __init__(self, product_id, producer_id, price, dfrom, dto, Lot_id, quan):
        self.Product_id = product_id
        self.Producer_id = producer_id
        self.price = price
        self.datefrom = dfrom
        self.dateto = dto
        self.Lotunit_id = Lot_id
        self.quantity = quan
