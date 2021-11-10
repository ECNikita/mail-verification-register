from rest_framework_swagger import renderers
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.shortcuts import render, redirect
from BarvaAPI.Models.registerModels import *
from rest_framework.response import Response
from BarvaAPI.serializer.registerSerialize import RegistrateSerialize
from rest_framework import status
from BarvaAPI.databaseProvider.registerCRUD import *
from django.http import JsonResponse
from rest_framework import status, permissions


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

class RegisterInsert(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    serializer_class = RegistrateSerialize

    def post(self, request):
        user_id = request.user.UserId
        user_data = JSONParser().parse(request)
        RegistrateSerializer = RegistrateSerialize(data=user_data)
        res = False
        if RegistrateSerializer.is_valid():
            res = insertdetails(RegistrateSerializer.data, user_id)

        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class RegisterUpdate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    serializer_class = RegistrateSerialize
    
    def put(self, request):
        user_id = request.user.UserId
        lot_data = JSONParser().parse(request)
        RegistrateSerializer = RegistrateSerialize(data=lot_data)
        valid_id = None
        if RegistrateSerializer.is_valid() and "Register_id" in RegistrateSerializer.data:
            valid_id = Validate_user_details(RegistrateSerializer.data["Register_id"])
        res = False
        
        if valid_id is not None and int(valid_id)==int(RegistrateSerializer.data["Register_id"]):
            res= updatedetails(RegistrateSerializer.data)
            
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

class DeleteRegisterUserByID(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    def delete(self, request):
        user_id = request.user.UserId
        uid = request.query_params.get('Register_id', None)
        res = False
        res = deletedetails(uid)

        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)