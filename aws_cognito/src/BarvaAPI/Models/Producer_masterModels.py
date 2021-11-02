from django.db import models


class Producer_masterModel(models.Model):
    Producer_id = models.BigIntegerField(blank=True,null=True)
    Producer_name = models.CharField(max_length=100) 
    Producer_address = models.CharField(max_length=100) 
    Producer_mobileno =  models.CharField(max_length=100) 
    Producer_adhaarno =  models.CharField(max_length=100) 
    Producer_email = models.CharField(max_length=100) 
    Producer_pancard = models.CharField(max_length=100) 
    Producer_gstno = models.CharField(max_length=100)
    Producer_firmregistration = models.CharField(max_length=100)

    def __init__(self,producer_id,name,address,mobileno,adhaarno,email,pancard,gstno,firmreg):
        self.Producer_id =producer_id
        self.Producer_name =name
        self.Producer_address = address
        self.Producer_mobileno =mobileno
        self.Producer_adhaarno = adhaarno
        self.Producer_email = email
        self.Producer_pancard = pancard
        self.Producer_gstno = gstno
        self.Producer_firmregistration = firmreg