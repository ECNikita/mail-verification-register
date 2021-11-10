from django.db import models

class WarehouseModel(models.Model):
    Warehouse_id = models.BigIntegerField(blank=True, null=True)
    Warehouse_name = models.CharField(max_length=100)
    Warehouse_address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=5)
    longitude = models.DecimalField(max_digits=9, decimal_places=5)
    Warehouse_capacity=models.BigIntegerField(blank=True, null=True)
    
    def __init__(self, id, name,addr,cap,lat,longit):
        self.Warehouse_id = id
        self.Warehouse_name = name
        self.Warehouse_address = addr
        self.Warehouse_capacity = cap
        self.latitude = lat
        self.longitude = longit
        