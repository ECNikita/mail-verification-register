from django.contrib import admin
from django.urls import path, include
from BarvaAPI.view.registerViews import RegisterUserByID,DeleteRegisterUserByID
from BarvaAPI.view.Product_masterViews import ProductInsert
from BarvaAPI.view.Producer_masterViews import ProducerInsert
from BarvaAPI.view.Lotunit_masterViews import LotInsert
from BarvaAPI.view.Product_pricebyproducerViews import *

urlpatterns = [
    path('registerbyid',RegisterUserByID.as_view()),
    path('deleteregister',DeleteRegisterUserByID.as_view()),

    path('productinsert',ProductInsert.as_view()),
   # path('deleteproduct',DeleteProduct.as_view()),

    path('producerinsert',ProducerInsert.as_view()),

    path('LotInsert',LotInsert.as_view()),

    path('productbyproducer',Product_pricebyproducerInsert.as_view()),

    path('getchart',GETchart.as_view())

]
