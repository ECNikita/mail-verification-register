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
import json
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

class RegisterUserByID(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    serializer_class = RegistrateSerialize

    def post(self, request):
        user_id = request.user.UserId
       # print('useris', user_id)
        user_data = JSONParser().parse(request)

        RegistrateSerializer = RegistrateSerialize(data=user_data)
       
        #print(user_id)
        # print(RegistrateSerializer.is_valid())
        #print(RegistrateSerializer.data)
        if RegistrateSerializer.is_valid():
            #user_id =RegistrateSerializer.data['UserId']
            #print(user_id)
            valid_user = Validate_user_details(user_id)
            res = False
            if valid_user is not None and valid_user == user_id:
                res = updatedetails(RegistrateSerializer.data, user_id)
            else:
                res = insertdetails(RegistrateSerializer.data, user_id)

            if res is True:
                data = {"res": "True"}
                return JsonResponse((data), safe=False)

        data = {"res": "False"}
        return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)


class DeleteRegisterUserByID(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    def delete(self, request):
        user_id = request.user.UserId
        res = False
        print("before server")
        res = deletedetails(user_id)

        if res is True:
            data = {"res":"True"}
            return JsonResponse((data), safe=False)
        else:
            data = {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)