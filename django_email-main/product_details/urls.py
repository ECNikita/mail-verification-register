from django.contrib import admin
from django.urls import path,include
from product_details import views

urlpatterns = [
    
    path('product_list',views.product_list),
]