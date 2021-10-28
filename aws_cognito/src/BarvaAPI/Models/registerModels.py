from django.db import models


class Register_details(models.Model):
    Register_id = models.BigIntegerField()
    UserId = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip = models.IntegerField(blank=True, null=True)
    Company = models.CharField(max_length=300)
    CompanyAddress = models.CharField(max_length=300)
    Phone_no = models.IntegerField(blank=True, null=True)

    def __init__(self, register_id, uid, firstname, lastname, address, city, state, zip, company, companyaddress, phone):
        self.Register_id = register_id
        self.UserId = uid
        self.Firstname = firstname
        self.Lastname = lastname
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zip
        self.Company = company
        self.CompanyAddress = companyaddress
        self.Phone_no = phone

    def to_object(d):
        register_id = d. d['Register_id']
        inst = Register_details(d['Register_id'], d['UserId'], d['Firstname'], d['Lastname'], d['Address'],
                                d['City'], d['State'], d['Zip'], d['Company'], d['CompanyAddress'], d['Phone_no'])

        return inst
