from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.Models.Producer_masterModels import Producer_masterModel
from rest_framework.response import Response
from BarvaAPI.serializer.Producer_masterSerialize import Producer_masterSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Producer_masterCRUD import *
from django.http import JsonResponse
import json
from rest_framework import status, permissions

class ProducerGET(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Producer_masterSerialize
    def get(self, request):
        prod_data = get_all_producer_details()
        Producer_masterSerializer = Producer_masterSerialize(data=prod_data, many=True)
        Producer_masterSerializer.is_valid()
        return JsonResponse(Producer_masterSerializer.data, safe=False)

class ProducerInsert(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Producer_masterSerialize
    def post(self, request):
        producer_data = JSONParser().parse(request)
        Producer_masterSerializer = Producer_masterSerialize(data=producer_data)
        
        res = False
        
        Producer_masterSerializer.is_valid()
        res = insertdetails(Producer_masterSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class ProducerUpdate(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
    serializer_class = Producer_masterSerialize
    def put(self, request):
        product_data = JSONParser().parse(request)
        Producer_masterSerializer = Producer_masterSerialize(data=product_data)
       
        if Producer_masterSerializer.is_valid() and "Producer_id" in Producer_masterSerializer.data:
            valid_id = Validate_product_details(Producer_masterSerializer.data["Producer_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(Producer_masterSerializer.data["Producer_id"]):
            res= updatedetails(Producer_masterSerializer.data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class DeleteProducer(generics.CreateAPIView):
    serializer_class = Producer_masterSerialize
    def delete(self, request):
        #product_data = JSONParser().parse(request)
        #Product_masterSerializer = Product_masterSerialize(data=product_data)
        
        uid = request.query_params.get('Producer_id', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)