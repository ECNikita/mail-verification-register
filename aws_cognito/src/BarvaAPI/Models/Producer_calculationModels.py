from django.db import models

class ProducerCalModel(models.Model):
    Product_id =models.BigIntegerField()
    finalprice =models.FloatField()
    producer_qty =models.FloatField()
    
    def __init__(self,p_id,finalprice,prod_qty):
        self.Product_id = p_id
        self.finalprice = finalprice
        self.producer_qty = prod_qty