from django.db import models

class UploadModel(models.Model):
    Pan_card = models.BinaryField()
    Aadhaar_card = models.BinaryField()
    Company_id = models.BinaryField()
    Photo = models.BinaryField()
    Pancard_file = models.CharField(max_length=1000)
    Aadhaarcard_file = models.CharField(max_length=1000)
    Companyid_file = models.CharField(max_length=1000)
    Photo_file = models.CharField(max_length=1000)

    def __init__(self,pancard,aadhaarcard,companyid , photo,pancard_file,aadhaarcard_file,companyid_file,photo_file):
        self.Pan_card = pancard
        self.Aadhaar_card = aadhaarcard
        self.Company_id = companyid
        self.Photo = photo
        self.Pancard_file = pancard_file
        self.Aadhaarcard_file =aadhaarcard_file
        self.Companyid_file = companyid_file
        self.Photo_file = photo_file



        
