from django.db import models


class Lotunit_masterModel(models.Model):
    Lotunit_id = models.BigIntegerField(blank=True, null=True)
    Lotunit_name = models.CharField(max_length=100)

    def __init__(self, lot_id, lot_name):
        self.Lotunit_id = lot_id
        self.Lotunit_name = lot_name
