from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Order_detailsSerialize import Order_detailsSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Order_detailsCRUD import *
from django.http import JsonResponse


class Order_detailsGET(generics.CreateAPIView):
    serializer_class = Order_detailsSerialize
    def get(self, request):
        order_data = get_all_Order_details()
        Order_detailsSerializer = Order_detailsSerialize(data=order_data, many=True)
        Order_detailsSerializer.is_valid()
        return JsonResponse(Order_detailsSerializer.data, safe=False)

class Order_detailsInsert(generics.CreateAPIView):
    serializer_class = Order_detailsSerialize
    def post(self, request):
        order_data = JSONParser().parse(request)
        Order_detailsSerializer = Order_detailsSerialize(data=order_data)
        res = False
        if Order_detailsSerializer.is_valid():
            res = insertdetails(Order_detailsSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class Order_detailsUpdate(generics.CreateAPIView):
    serializer_class = Order_detailsSerialize
    def put(self, request):
        order_data = JSONParser().parse(request)
        Order_detailsSerializer = Order_detailsSerialize(data=order_data)
       
        if Order_detailsSerializer.is_valid() and "Order_id" in Order_detailsSerializer.data:
            valid_id = Validate_product_details(Order_detailsSerializer.data["Order_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Order_detailsSerializer.data["Order_id"]):
            res= updatedetails(Order_detailsSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class Order_detailsDelete(generics.CreateAPIView):
    serializer_class = Order_detailsSerialize
    def delete(self, request):
        uid = request.query_params.get('Order_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)