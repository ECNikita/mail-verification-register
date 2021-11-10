from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Producer_paymentdetailsSerialize import Producer_paymentdetailsSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Producer_paymentdetailsCRUD import *
from django.http import JsonResponse


class Producer_paymentGET(generics.CreateAPIView):
    serializer_class = Producer_paymentdetailsSerialize
    def get(self, request):
        prod_data = get_all_Producer_payment_details()
        Producer_paymentdetailsSerializer = Producer_paymentdetailsSerialize(data=prod_data, many=True)
        Producer_paymentdetailsSerializer.is_valid()
        return JsonResponse(Producer_paymentdetailsSerializer.data, safe=False)

class Producer_paymentInsert(generics.CreateAPIView):
    serializer_class = Producer_paymentdetailsSerialize
    def post(self, request):
        prod_data = JSONParser().parse(request)
        Producer_paymentdetailsSerializer = Producer_paymentdetailsSerialize(data=prod_data)
        res = False
        if Producer_paymentdetailsSerializer.is_valid():
            res = insertdetails(Producer_paymentdetailsSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class Producer_paymentUpdate(generics.CreateAPIView):
    serializer_class = Producer_paymentdetailsSerialize
    def put(self, request):
        prod_data = JSONParser().parse(request)
        Producer_paymentdetailsSerializer = Producer_paymentdetailsSerialize(data=prod_data)
        
        if Producer_paymentdetailsSerializer.is_valid() and "Customer_commisionpay_id" in Producer_paymentdetailsSerializer.data:
            valid_id = Validate_product_details(Producer_paymentdetailsSerializer.data["Customer_commisionpay_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Producer_paymentdetailsSerializer.data["Customer_commisionpay_id"]):
            res= updatedetails(Producer_paymentdetailsSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class Producer_paymentDelete(generics.CreateAPIView):
    serializer_class = Producer_paymentdetailsSerialize
    def delete(self, request):
        uid = request.query_params.get('Customer_commisionpay_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)