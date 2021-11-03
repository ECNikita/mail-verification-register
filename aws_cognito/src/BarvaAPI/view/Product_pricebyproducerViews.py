from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Product_pricebyproducerSerialize import Product_pricebyproducerSerialize
from rest_framework import status
from BarvaAPI.serializer.chartinputSerialize import *
from BarvaAPI.databaseProvider.Product_pricebyproducerCRUD import *
from BarvaAPI.databaseProvider.chartinputCRUD import *
from django.http import JsonResponse


class Product_pricebyproducerGET(generics.CreateAPIView):
    serializer_class = Product_pricebyproducerSerialize
    def get(self, request):
        prod_data = get_all_product_price_details()
        Product_pricebyproducerSerializer = Product_pricebyproducerSerialize(data=prod_data, many=True)
        Product_pricebyproducerSerializer.is_valid()
        return JsonResponse(Product_pricebyproducerSerializer.data, safe=False)

class Product_pricebyproducerInsert(generics.CreateAPIView):
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

class Product_pricebyproducerUpdate(generics.CreateAPIView):
    serializer_class = Product_pricebyproducerSerialize
    def put(self, request):
        Prod_data = JSONParser().parse(request)
        Product_pricebyproducerSerializer = Product_pricebyproducerSerialize(data=Prod_data)
        res = False
        

        if Product_pricebyproducerSerializer.is_valid() and "Serial_id" in Product_pricebyproducerSerializer.data:
            valid_id = Validate_product_details(Product_pricebyproducerSerializer.data["Serial_id"])
            
        if valid_id is not None and int(valid_id) == int(Product_pricebyproducerSerializer.data["Serial_id"]):
            res = updatedetails(Product_pricebyproducerSerializer.data)
            
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class Product_pricebyproducerDelete(generics.CreateAPIView):
    serializer_class = Product_pricebyproducerSerialize
    def delete(self, request):
        
        uid = request.query_params.get('Serial_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class GETquanchart(generics.CreateAPIView):
    serializer_class = ChartSerialize
    def post(self, request):
        Product_data = JSONParser().parse(request)
        ChartSerializer = ChartSerialize(data=Product_data)
        if ChartSerializer.is_valid():
            res = get_all_chart_quan_details(ChartSerializer.data)
            serializer = ChartResponseSerialize(data=res,many=True)
            serializer.is_valid()
            return JsonResponse((serializer.data), safe=False)