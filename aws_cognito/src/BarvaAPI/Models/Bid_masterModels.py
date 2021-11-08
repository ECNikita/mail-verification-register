from django.db import models


class Bid_masterModel(models.Model):
    Bidtype_id = models.BigIntegerField(blank=True ,null=True)
    Bidtype_name = models.CharField(max_length=100)

    def __init__(self,bid_id,bid_name):
        self.Bidtype_id = bid_id
        self.Bidtype_name = bid_name