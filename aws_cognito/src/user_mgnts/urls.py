from django.contrib import admin
from django.urls import path, include
from user_mgnts import views


urlpatterns = [
    # path('signup',views.sign_up),
    path('signup', views.sign_up.as_view()),
    path('auth',views.GetDataView.as_view()),
    path('confirm_signup', views.confirm_sign_up.as_view()),
    path('resend_confirm', views.resend_confirm_code.as_view()),
    path('signin', views.sign_in.as_view()),
    path('get_user', views.get_user.as_view()),
    path('confirm_forgot_password', views.confirm_forgot_password.as_view()),
    path('forgot_password', views.forgot_password.as_view()),
    path('change_password', views.change_password.as_view()),


]
