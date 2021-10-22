from django.contrib import admin
from django.urls import path,include
from uploadImageapp import views

urlpatterns = [
    
    path('uploadimage' ,  views.upload_doc_list),
]