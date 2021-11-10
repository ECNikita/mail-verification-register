from django.db import models


class Order_detailsModel(models.Model):
    Order_id = models.BigIntegerField(blank=True ,null=True)
    Customer_commisionpay_id = models.BigIntegerField(blank=True ,null=True)
    Request_id = models.BigIntegerField(blank=True ,null=True)
    Order_date = models.DateTimeField()
    Order_price = models.IntegerField()
    
    def __init__(self,ord_id,cust_id,req_id,ord_date,ord_price):
        self.Order_id = ord_id 
        self.Customer_commisionpay_id = cust_id
        self.Request_id = req_id
        self.Order_date = ord_date
        self.Order_price = ord_price 