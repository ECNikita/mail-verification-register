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
        
        if Producer_masterSerializer.is_valid():
            res = insertdetails(Producer_masterSerializer.data)
            
        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
