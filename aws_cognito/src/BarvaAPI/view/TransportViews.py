from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.TransportSerialize import TransportSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.TransportCRUD import *
from django.http import JsonResponse


class TransportGET(generics.CreateAPIView):
    serializer_class = TransportSerialize
    def get(self, request):
        trans_data = get_all_transport_details()
        TransportSerializer = TransportSerialize(data=trans_data, many=True)
        TransportSerializer.is_valid()
        return JsonResponse(TransportSerializer.data, safe=False)

class TransportInsert(generics.CreateAPIView):
    serializer_class = TransportSerialize
    def post(self, request):
        trans_data = JSONParser().parse(request)
        TransportSerializer = TransportSerialize(data=trans_data)
        print(TransportSerializer.is_valid())
        print(TransportSerializer.errors)
        res = False
        if TransportSerializer.is_valid():
            print(TransportSerializer.errors)
            res = insertdetails(TransportSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class TransportUpdate(generics.CreateAPIView):
    serializer_class = TransportSerialize
    def put(self, request):
        trans_data = JSONParser().parse(request)
        TransportSerializer = TransportSerialize(data=trans_data)
       
        if TransportSerializer.is_valid() and "Transport_id" in TransportSerializer.data:
            valid_id = Validate_product_details(TransportSerializer.data["Transport_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(TransportSerializer.data["Transport_id"]):
            res= updatedetails(TransportSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class TransportDelete(generics.CreateAPIView):
    serializer_class = TransportSerialize
    def delete(self, request):
        uid = request.query_params.get('Transport_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)