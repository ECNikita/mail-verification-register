from django.contrib import admin
from django.urls import path, include
from trade_details import views

urlpatterns = [

    path('trade_list', views.trade_list),
]
