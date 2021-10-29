from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.Models.Product_pricebyproducerModels import Product_pricebyproducerModel
from BarvaAPI.Models.chartinputModels import *
from rest_framework.response import Response
from BarvaAPI.serializer.Product_pricebyproducerSerialize import Product_pricebyproducerSerialize
from rest_framework import status
from BarvaAPI.serializer.chartinputSerialize import *
from BarvaAPI.databaseProvider.Product_pricebyproducerCRUD import *
from BarvaAPI.databaseProvider.chartinputCRUD import *
from django.http import JsonResponse
import json
from rest_framework import status, permissions

class Product_pricebyproducerInsert(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Product_pricebyproducerSerialize
    def post(self, request):
        Product_data = JSONParser().parse(request)
        Product_pricebyproducerSerializer = Product_pricebyproducerSerialize(data=Product_data)
        res = False
        if Product_pricebyproducerSerializer.is_valid():
            res = insertdetails(Product_pricebyproducerSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class GETchart(generics.CreateAPIView):
    serializer_class = ChartSerialize
    def post(self, request):
        Product_data = JSONParser().parse(request)
        ChartSerializer = ChartSerialize(data=Product_data)
        if ChartSerializer.is_valid():
            res = get_all_chart_details(ChartSerializer.data)
            serializer = ChartResponseSerialize(data=res ,many=True)
            serializer.is_valid()
            return JsonResponse((serializer.data), safe=False)

