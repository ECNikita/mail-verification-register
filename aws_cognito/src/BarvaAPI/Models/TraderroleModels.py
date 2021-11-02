from django.db import models


class TraderroleModel(models.Model):
    Traderrole_id = models.BigIntegerField(blank=True, null=True)
    Traderrole_name = models.CharField(max_length=100)

    def __init__(self, trader_id, trader_name):
        self.Traderrole_id = trader_id
        self.Traderrole_name = trader_name
