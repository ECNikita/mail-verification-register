from rest_framework.parsers import JSONParser 
from types import SimpleNamespace
from django.shortcuts import render,redirect
from register_details.models import Register_details
from rest_framework.views import APIView
from rest_framework.response import Response
from register_details.serialize import RegistrateSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from register_details.databaseProvider.User_detailsCRUD import *
from django.http import JsonResponse
import json

@api_view(['GET', 'POST', 'DELETE'])
def register_list(request):
    if request.method == 'GET':
        registers = get_all_register_details()
        
        uids = request.query_params.get('uid', None)
        
        if uids is not None:
            for x in registers:     
                if int(x.uid) == int(uids):
                    registers=[x]
                    break

        RegistrateSerializer = RegistrateSerialize(registers, many=True)
        return JsonResponse(RegistrateSerializer.data, safe=False)


    elif request.method == 'POST':
        register_data = json.loads(request.body)
        print(register_data)
        valid_user = Validate_user_details(register_data["UserId"])
        res = False
        if valid_user is not None and int(valid_user)==int(register_data["UserId"]):
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
