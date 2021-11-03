from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.Lotunit_masterSerialize import Lotunit_masterSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Lotunit_masterCRUD import *
from django.http import JsonResponse


class LotGET(generics.CreateAPIView):
    serializer_class = Lotunit_masterSerialize
    def get(self, request):
        prod_data = get_all_Lot_details()
        Lotunit_masterSerializer = Lotunit_masterSerialize(data=prod_data, many=True)
        Lotunit_masterSerializer.is_valid()
        return JsonResponse(Lotunit_masterSerializer.data, safe=False)

class LotInsert(generics.CreateAPIView):
    serializer_class = Lotunit_masterSerialize
    def post(self, request):
        Lot_data = JSONParser().parse(request)
        Lotunit_masterSerializer = Lotunit_masterSerialize(data=Lot_data)
        res = False
        if Lotunit_masterSerializer.is_valid():
            res = insertdetails(Lotunit_masterSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class LotUpdate(generics.CreateAPIView):
    serializer_class = Lotunit_masterSerialize
    def put(self, request):
        lot_data = JSONParser().parse(request)
        Lotunit_masterSerializer = Lotunit_masterSerialize(data=lot_data)
       
        if Lotunit_masterSerializer.is_valid() and "Lotunit_id" in Lotunit_masterSerializer.data:
            valid_id = Validate_product_details(Lotunit_masterSerializer.data["Lotunit_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Lotunit_masterSerializer.data["Lotunit_id"]):
            res= updatedetails(Lotunit_masterSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class LotDelete(generics.CreateAPIView):
    serializer_class = Lotunit_masterSerialize
    def delete(self, request):
        uid = request.query_params.get('Lotunit_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)