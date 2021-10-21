from django.db import models

class Register_details(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip = models.IntegerField(blank=True, null=True)
    Company = models.CharField(max_length=300)
    CompanyAddress = models.CharField(max_length=300)
    Phone_no = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table=""