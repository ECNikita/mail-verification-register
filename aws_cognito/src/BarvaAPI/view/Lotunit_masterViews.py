from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.Models.Lotunit_masterModels import Lotunit_masterModel
from rest_framework.response import Response
from BarvaAPI.serializer.Lotunit_masterSerialize import Lotunit_masterSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.Lotunit_masterCRUD import *
from django.http import JsonResponse
import json
from rest_framework import status, permissions


class LotInsert(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = [
    #     renderers.OpenAPIRenderer,
    #     renderers.SwaggerUIRenderer
    # ]
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