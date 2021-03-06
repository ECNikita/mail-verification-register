from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from user_mgnts.views import *
from django.views.generic import TemplateView
from BarvaAPI.view import *
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='BARVA API')
# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Users API', renderer_classes=[
                             OpenAPIRenderer, SwaggerUIRenderer])
urlpatterns = [
    path('openapi/', get_schema_view(title="Barva Organic Commodities"), name='openapi-schema'),
    path('docs/', TemplateView.as_view(template_name='documentation.html',extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('users/', include('user_mgnts.urls')),
    path('',include('BarvaAPI.urls')),
    path('chart/', TemplateView.as_view(template_name='examplechart.html' ))
]
