from django.contrib import admin
from django.urls import path, include
from BarvaAPI.view.registerViews import *

urlpatterns = [
    path('registerbyid',RegisterUserByID.as_view()),
    path('deletebyid',DeleteRegisterUserByID.as_view())
    
]
