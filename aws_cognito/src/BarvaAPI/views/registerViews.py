from rest_framework.parsers import JSONParser
from rest_framework import generics 
from types import SimpleNamespace
from django.shortcuts import render,redirect
from BarvaAPI.Models.registerModels import Register_details
from rest_framework.views import APIView
from rest_framework.response import Response
from BarvaAPI.serializer.registerSerialize import RegistrateSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from BarvaAPI.databaseProvider.registerCRUD import *
from django.http import JsonResponse
import json

# class GetAllRegisterUser(generics.CreateAPIView):
#     def get(self, request):
#             registers = get_all_register_details()
#             uids = request.query_params.get('uid', None)
            
#             if uids is not None:
#                 for x in registers:     
#                     if int(x.uid) == int(uids):
#                         registers=[x]
#                         break

#             RegistrateSerializer = RegistrateSerialize(registers, many=True)
#             return JsonResponse(RegistrateSerializer.data, safe=False)

class GetRegisterUserByID(generics.CreateAPIView):
    serializer_class = RegistrateSerialize
    def post(self, request):
        user_data = JSONParser().parse(request.user.UserId)
        RegistrateSerializer = RegistrateSerialize(data=user_data)
        if RegistrateSerializer.is_valid():
            valid_user = Validate_user_details(user_data)
            res = False
            if valid_user is not None and int(valid_user)==int(register_data["uid"]):
                res= updatedetails(register_data)
            else:
                res = insertdetails(register_data)
            
            if res is True:
                data= {"res":"True"}
                return JsonResponse((data), safe=False)
            else :
                data= {"res":"False"}
                return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uid = request.query_params.get('uid', None)
        
        res=False
        res = deletedetails(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
