from django.contrib import admin
from django.urls import path,include
from accounts import views
from register_details.views import *


urlpatterns = [
   
    path('user_list',views.user_list),
    path('activate_user',views.activate_user),
    
    path('saveapp/',include('register_details.urls')),
   
]