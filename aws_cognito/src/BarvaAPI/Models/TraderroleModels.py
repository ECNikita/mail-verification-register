from django.db import models


class Traderrole_Model(models.Model):
    Traderrole_id = models.BigIntegerField(blank=True, null=True,primary_key=True)
    Traderrole_name = models.CharField(max_length=100)

    def __init__(self, traderrole_id, traderrole_name):
        self.Traderrole_id = traderrole_id
        self.Traderrole_name = traderrole_name
