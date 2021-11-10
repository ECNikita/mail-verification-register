from django.db import models

class TransportModel(models.Model):
    Transport_id = models.BigIntegerField(blank=True, null=True)
    Transport_name = models.CharField(max_length=100)
    Transport_address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #Transport_geolocation = models.PointField()
    Transport_firmregistration= models.CharField(max_length=100)
    Transport_frim_pancard = models.CharField(max_length=100)
    
    def __init__(self, id, name,addr,firmreg,firmpan,lat,longit):
        self.Transport_id = id
        self.Transport_name = name
        self.Transport_address = addr
        self.Transport_firmregistration = firmreg
        self.Transport_frim_pancard = firmpan
        self.latitude = lat
        self.longitude = longit