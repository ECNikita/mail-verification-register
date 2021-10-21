from django.db import models

class UploadModel(models.Model):
    Pan_card = models.FileField()
    Aadhaar_card = models.FileField()
    Company_document = models.FileField()
    Photo = models.FileField()

#upload_to = "profiles", height_field = 300 ,width_field = 342