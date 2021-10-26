"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from register_details.views import *
from uploadImageapp.views import *
from samplechart.views import *
from product_details.views import *
from trade_details.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="rest API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@rest.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('saveapp', include('register_details.urls')),
    path('upload', include('uploadImageapp.urls')),
    path('chart/', include('samplechart.urls')),
    path('products/', include('product_details.urls')),
    path('trade/', include('trade_details.urls')),
]
