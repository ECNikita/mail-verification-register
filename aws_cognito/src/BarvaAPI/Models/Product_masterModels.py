from django.db import models


class Product_masterModel(models.Model):
    Product_id = models.BigIntegerField(blank=True,null=True)
    Product_name = models.CharField(max_length=100) 
    Product_size = models.CharField(max_length=100)
    Product_season = models.CharField(max_length=100)
    Product_fractionalreserve = models.BigIntegerField()

    def __init__(self,product_id,product_name,product_size,product_season,product_frac):
        self.Product_id = product_id
        self.Product_name = product_name
        self.Product_size = product_size
        self.Product_season = product_season
        self.Product_fractionalreserve = product_frac
        