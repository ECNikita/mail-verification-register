from django.db import models


class BidProductModel(models.Model):
    startdate =models.DateTimeField()
    todate =models.DateTimeField()

    def __init__(self,start_dt,to_dt):
        self.startdate = start_dt
        self.todate = to_dt
        
class BidCalModel(models.Model):
    Product_id =models.BigIntegerField()
    percentage =models.FloatField()
    finalprice =models.FloatField()
    
    def __init__(self,p_id,per,finalprice):
        self.Product_id = p_id
        self.percentage = per
        self.finalprice = finalprice
        