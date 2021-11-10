from django.db import models


class Register_details(models.Model):
    Register_id = models.BigIntegerField()
    #UserId = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip = models.IntegerField(blank=True, null=True)
    Firm = models.CharField(max_length=300)
    Firm_pan = models.CharField(max_length=300)
    Phoneno = models.BigIntegerField()
    Gst_no = models.CharField(max_length=300)
    Credit_limit = models.IntegerField(blank=True, null=True)
    Registration_date = models.DateTimeField()
    Wallet = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __init__(self, register_id, firstname, lastname, address, city, state, zip, firm, firm_pan, phone,gst,lim,reg_date,wall,lat,long):
        self.Register_id = register_id
        #self.UserId = uid
        self.Firstname = firstname
        self.Lastname = lastname
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zip
        self.Firm = firm
        self.Firm_pan = firm_pan
        self.Phoneno = phone
        self.Gst_no = gst
        self.Credit_limit = lim
        self.Registration_date = reg_date
        self.Wallet = wall
        self.latitude = lat
        self.longitude = long

    # def to_object(d):
    #     register_id = d. d['Register_id']
    #     inst = Register_details(d['Register_id'], d['Firstname'], d['Lastname'], d['Address'],
    #                             d['City'], d['State'], d['Zip'], d['Firm'], d['FirmAddress'], d['Phoneno'])

    #     return inst
