from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.CustomerProducer_Bid_detailsSerialize import CustomerProducer_Bid_detailsSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.CustomerProducer_Bid_detailsCRUD import *
from django.http import JsonResponse


class CustBidGet(generics.CreateAPIView):
    serializer_class = CustomerProducer_Bid_detailsSerialize
    def get(self, request):
        prod_data = get_all_Cust_details()
        CustomerProducer_Bid_detailsSerializer = CustomerProducer_Bid_detailsSerialize(data=prod_data, many=True)
        CustomerProducer_Bid_detailsSerializer.is_valid()
        return JsonResponse(CustomerProducer_Bid_detailsSerializer.data, safe=False)

class CustBidInsert(generics.CreateAPIView):
    serializer_class = CustomerProducer_Bid_detailsSerialize
    def post(self, request):
        Bid_data = JSONParser().parse(request)
        CustomerProducer_Bid_detailsSerializer = CustomerProducer_Bid_detailsSerialize(data=Bid_data)
        res = False
       
        if CustomerProducer_Bid_detailsSerializer.is_valid():
            res = insertdetails(CustomerProducer_Bid_detailsSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class CustBidUpdate(generics.CreateAPIView):
    serializer_class = CustomerProducer_Bid_detailsSerialize
    def put(self, request):
        Bid_data = JSONParser().parse(request)
        CustomerProducer_Bid_detailsSerializer = CustomerProducer_Bid_detailsSerialize(data=Bid_data)
        print(CustomerProducer_Bid_detailsSerializer)
        print(CustomerProducer_Bid_detailsSerializer.is_valid)
        if CustomerProducer_Bid_detailsSerializer.is_valid() and "Request_id" in CustomerProducer_Bid_detailsSerializer.data:
            valid_id = Validate_product_details(CustomerProducer_Bid_detailsSerializer.data["Request_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(CustomerProducer_Bid_detailsSerializer.data["Request_id"]):
            res= updatedetails(CustomerProducer_Bid_detailsSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class CustBidDelete(generics.CreateAPIView):
    serializer_class = CustomerProducer_Bid_detailsSerialize
    def delete(self, request):
        uid = request.query_params.get('Request_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)