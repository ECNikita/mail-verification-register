from django.urls import path
from samplechart import views
from django.contrib import admin

urlpatterns = [
    path('get_chart_data',  views.get_chart_data),
    path('viewchart', views.view_chart),
]
