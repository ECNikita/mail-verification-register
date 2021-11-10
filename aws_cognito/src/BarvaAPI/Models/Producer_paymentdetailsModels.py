from django.db import models


class Producer_paymentdetailsModel(models.Model):
    Customer_commisionpay_id = models.BigIntegerField(blank=True ,null=True)
    Request_id = models.BigIntegerField(blank=True ,null=True)
    Register_id = models.BigIntegerField(blank=True ,null=True)
    Payment_date = models.DateTimeField()
    Payment_amount = models.IntegerField()
    Wallet_details = models.CharField(max_length=100)
    
    def __init__(self,cust_id,req_id,Reg_id,pay_date,pay_amt,wallet):
        self.Customer_commisionpay_id = cust_id
        self.Request_id = req_id
        self.Register_id = Reg_id
        self.Payment_date = pay_date
        self.Payment_amount = pay_amt
        self.Wallet_details = wallet