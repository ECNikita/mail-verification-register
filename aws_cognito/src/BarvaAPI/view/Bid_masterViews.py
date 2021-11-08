from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Bid_masterSerialize import Bid_masterSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Bid_masterCRUD import *
from django.http import JsonResponse


class BidGet(generics.CreateAPIView):
    serializer_class = Bid_masterSerialize
    def get(self, request):
        prod_data = get_all_bid_details()
        Bid_masterSerializer = Bid_masterSerialize(data=prod_data, many=True)
        Bid_masterSerializer.is_valid()
        return JsonResponse(Bid_masterSerializer.data, safe=False)

class BidInsert(generics.CreateAPIView):
    serializer_class = Bid_masterSerialize
    def post(self, request):
        Bid_data = JSONParser().parse(request)
        Bid_masterSerializer = Bid_masterSerialize(data=Bid_data)
        res = False
        if Bid_masterSerializer.is_valid():
            res = insertdetails(Bid_masterSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class BidUpdate(generics.CreateAPIView):
    serializer_class = Bid_masterSerialize
    def put(self, request):
        Bid_data = JSONParser().parse(request)
        Bid_masterSerializer = Bid_masterSerialize(data=Bid_data)
       
        if Bid_masterSerializer.is_valid() and "Bidtype_id" in Bid_masterSerializer.data:
            valid_id = Validate_product_details(Bid_masterSerializer.data["Bidtype_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Bid_masterSerializer.data["Bidtype_id"]):
            res= updatedetails(Bid_masterSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class BidDelete(generics.CreateAPIView):
    serializer_class = Bid_masterSerialize
    def delete(self, request):
        uid = request.query_params.get('Bidtype_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)