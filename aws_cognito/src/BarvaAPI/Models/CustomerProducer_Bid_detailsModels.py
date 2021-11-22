from django.db import models


class CustomerProducer_Bid_detailsModel(models.Model):
    Request_id = models.BigIntegerField(blank=True ,null=True)
    Producer_id  = models.BigIntegerField(blank=True ,null=True)
    Register_id  = models.BigIntegerField(blank=True ,null=True)
    Product_id = models.BigIntegerField(blank=True ,null=True)
    Producerproductprice = models.IntegerField()
    Customer_bidprice = models.IntegerField()
    DateTime = models.DateTimeField()
    Bidtype_id =  models.BigIntegerField(blank=True ,null=True)
    Quantity = models.IntegerField()
    Trader_notification = models.CharField(max_length=100)
    Trader_approval = models.CharField(max_length=100)
    Approval_comments = models.CharField(max_length=100)

    def __init__(self,req_id,Prod_id,reg_id,Pro_id,Prodpro,cust_bid,dates,bid_id,quan,tra_not,tra_app,app_com):
        self.Request_id= req_id
        self.Producer_id = Prod_id
        self.Register_id = reg_id
        self.Product_id = Pro_id
        self.Producerproductprice = Prodpro
        self.Customer_bidprice = cust_bid
        self.DateTime = dates
        self.Bidtype_id = bid_id
        self.Quantity = quan
        self.Trader_notification = tra_not
        self.Trader_approval = tra_app
        self.Approval_comments = app_com
        