from django.db import models

class Trade_detailsModel(models.Model):
    Trade_id  =  models.BigIntegerField()
    Product_id = models.BigIntegerField()
    uid = models.BigIntegerField()
    Date = models.DateField()
    Quantity = models.BigIntegerField()
    Price = models.BigIntegerField()
    
    def __init__(self, t_id,p_id,u_id,date,quantity,price):
        self.Trade_id = t_id
        self.Product_id = p_id
        self.uid = u_id
        self.Date = date
        self.Quantity = quantity
        self.Price = price