from django.contrib import admin
from django.urls import path,include
from accounts import views
from register_details.views import *


urlpatterns = [
   
    path('user_list',views.user_list),
    path('activate_user',views.activate_user),
    #path('')
    # path('' ,  home  , name="home"),
    # path('register' , register_attempt , name="register_attempt"),
    # path('accounts/login/' , login_attempt , name="login_attempt"),
    # path('token' , token_send , name="token_send"),
    # path('success' , success , name='success'),
    # path('verifyotp' , verifyotp , name="verifyotp"),
    # path('error' , error_page , name="error"),
    path('saveapp/',include('register_details.urls')),
   
]