from django.shortcuts import render,redirect
from register_details.models import Register_details
from rest_framework.views import APIView
from rest_framework.response import Response
from uploadImageapp.serialize import UploadSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from uploadImageapp.databaseProvider.upload_documentsCRUD import *
from django.http import JsonResponse
import json
from rest_framework.parsers import JSONParser 

@api_view(['GET', 'POST', 'DELETE'])
def upload_doc_list(request):
    if request.method == 'GET':
        upload_doc = user_upload_doc()
        
        uids = request.query_params.get('uid', None)
        
        if uids is not None:
            for x in upload_doc:     
                if int(x.uid) == int(uids):
                    upload_doc=[x]
                    break

        UploadSerializer = UploadSerialize(upload_doc, many=True)
        return JsonResponse(UploadSerializer.data, safe=False)

    elif request.method == 'POST':
        upload_data = json.loads(request.body)
        print(register_data)
        valid_user = Validate_user_detail(upload_data["uid"])
        res = False
        if valid_user is not None and int(valid_user)==int(upload_data["uid"]):
            res= Update_upload_doc(upload_data)
        else:
            res = Insert_upload_doc(upload_data)
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uid = request.query_params.get('uid', None)
        
        res=False
        res = delete_details(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)








