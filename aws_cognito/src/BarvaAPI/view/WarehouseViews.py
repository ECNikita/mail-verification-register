from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.serializer.WarehouseSerialize import WarehouseSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.WarehouseCRUD import *
from django.http import JsonResponse


class WarehouseGET(generics.CreateAPIView):
    serializer_class = WarehouseSerialize
    def get(self, request):
        warehouse_data = get_all_warehouse_details()
        WarehouseSerializer = WarehouseSerialize(data=warehouse_data, many=True)
        WarehouseSerializer.is_valid()
        return JsonResponse(WarehouseSerializer.data, safe=False)

class WarehouseInsert(generics.CreateAPIView):
    serializer_class = WarehouseSerialize
    def post(self, request):
        warehouse_data = JSONParser().parse(request)
        WarehouseSerializer = WarehouseSerialize(data=warehouse_data)
        res = False
        if WarehouseSerializer.is_valid():
            res = insertdetails(WarehouseSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class WarehouseUpdate(generics.CreateAPIView):
    serializer_class = WarehouseSerialize
    def put(self, request):
        warehouse_data = JSONParser().parse(request)
        WarehouseSerializer = WarehouseSerialize(data=warehouse_data)
       
        if WarehouseSerializer.is_valid() and "Warehouse_id" in WarehouseSerializer.data:
            valid_id = Validate_product_details(WarehouseSerializer.data["Warehouse_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(WarehouseSerializer.data["Warehouse_id"]):
            res= updatedetails(WarehouseSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class WarehouseDelete(generics.CreateAPIView):
    serializer_class = WarehouseSerialize
    def delete(self, request):
        uid = request.query_params.get('Warehouse_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)