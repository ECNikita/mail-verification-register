from django.contrib import admin
from django.urls import path,include
from register_details import views

urlpatterns = [
    
    path('register_list',views.register_list),
]