from django.db import models


class Trader_detailsModel(models.Model):
    Trader_id = models.BigIntegerField(blank=True ,null=True)
    Traderrole_id = models.BigIntegerField(blank=True ,null=True)
    Trader_name = models.CharField(max_length=100)
    Trader_email = models.CharField(max_length=100)
    Trader_mobile = models.BigIntegerField(blank=True ,null=True)

    def __init__(self,trad_id,trader_id,trad_name,trad_email,trad_mobile):
        self.Traderrole_id = trad_id
        self.Trader_name = trad_name
        self.Trader_email = trad_email
        self.Trader_id = trader_id
        self.Trader_mobile = trad_mobile