from django.db import models


class Product_detailsModel(models.Model):
    Product_id = models.BigIntegerField()
    Product_name = models.CharField(max_length=100)
    Product_size = models.BigIntegerField()
    Product_price = models.BigIntegerField()

    def __init__(self, p_id, product_name, product_size, product_price):
        self.Product_id = p_id
        self.Product_name = product_name
        self.Product_price = product_price
        self.Product_size = product_size
