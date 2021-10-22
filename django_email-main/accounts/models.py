from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    uid = models.BigIntegerField(max_length=100 )
    Email = models.CharField(max_length=100 )
    Password = models.CharField(max_length=100 )
    IsActive = models.BooleanField(default=False)
    otp = models.IntegerField(max_length=100)


#uid, "Email", "Password", "IsActive", otp
    def __init__(self,uid,email,password,isactive,otp):
        self.uid = uid
        self.Email = email
        self.Password = password
        self.IsActive = isactive
        self.otp = otp


