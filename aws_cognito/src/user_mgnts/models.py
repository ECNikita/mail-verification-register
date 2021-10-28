from django.db import models


class CognitoUserModel(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __init__(self, email, password):
        self.Email = email
        self.Password = password

class UserIdModel(models.Model):
    UserId = models.CharField(max_length=100000)
    is_authenticated = models.BooleanField()
    
    def __init__(self,uid,auth):
        self.UserId=uid
        self.is_authenticated = auth

class SigninModel(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __init__(self, email, password):
        self.Email = email
        self.Password = password


class ConfirmSignupModel(models.Model):
    Email = models.CharField(max_length=100)
    confirm_code = models.CharField(max_length=100)

    def __init__(self, email, confirm):
        self.Email = email
        self.confirm_code = confirm


class ResendConfirmcodeModel(models.Model):
    Email = models.CharField(max_length=100)

    def __init__(self, email):
        self.Email = email

class ForgotPasswordModel(models.Model):
    Email = models.CharField(max_length=100)

    def __init__(self, email):
        self.Email = email

class GetUserModel(models.Model):
    AccessToken = models.CharField(max_length=10000)
    
    def __init__(self, accesstoken):
            self.AccessToken = accesstoken

class ConfirmForgotPasswordModel(models.Model):
    Email = models.CharField(max_length=100)
    confirm_code = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __init__(self, email, confirm,password):
        self.Email = email
        self.confirm_code = confirm
        self.Password = password

class ChangePasswordModel(models.Model):
    AccessToken = models.CharField(max_length=10000)
    NewPassword = models.CharField(max_length=100)
    PreviousPassword = models.CharField(max_length=100)

    def __init__(self, acess, newpassword,prevpassword):
        self.AccessToken = acess
        self.NewPassword = newpassword
        self.PreviousPasswordPassword = prevpassword


