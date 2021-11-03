from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.response import Response
from BarvaAPI.serializer.Trader_detailsSerialize import Trader_detailsSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Trader_detailsCRUD import *
from django.http import JsonResponse


class Trader_detailsGET(generics.CreateAPIView):
    serializer_class = Trader_detailsSerialize
    def get(self, request):
        trader_data = get_all_trader_details()
        Trader_detailsSerializer = Trader_detailsSerialize(data=trader_data, many=True)
        Trader_detailsSerializer.is_valid()
        return JsonResponse(Trader_detailsSerializer.data, safe=False)

class Trader_detailsInsert(generics.CreateAPIView):
    serializer_class = Trader_detailsSerialize
    def post(self, request):
        Lot_data = JSONParser().parse(request)
        Trader_detailsSerializer = Trader_detailsSerialize(data=Lot_data)
        res = False
        if Trader_detailsSerializer.is_valid():
            res = insertdetails(Trader_detailsSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class Trader_detailsUpdate(generics.CreateAPIView):
    serializer_class = Trader_detailsSerialize
    def put(self, request):
        lot_data = JSONParser().parse(request)
        Trader_detailsSerializer = Trader_detailsSerialize(data=lot_data)
       
        if Trader_detailsSerializer.is_valid() and "Trader_id" in Trader_detailsSerializer.data:
            valid_id = Validate_product_details(Trader_detailsSerializer.data["Trader_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Trader_detailsSerializer.data["Trader_id"]):
            res= updatedetails(Trader_detailsSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class Trader_detailsDelete(generics.CreateAPIView):
    serializer_class = Trader_detailsSerialize
    def delete(self, request):
        uid = request.query_params.get('Trader_id', None)
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)