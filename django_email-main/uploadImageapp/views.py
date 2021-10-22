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








# @api_view(['POST'])
# def index(request):
#     if request.method == "POST":
#         saveserialize = UploadSerialize(data=request.data)
#         if saveserialize.is_valid():
#             saveserialize.save()
#             return Response(saveserialize.data,status=status.HTTP_201_CREATED)
#             return Response(saveserialize.data , status = status.HTTP_400_BAD_REQUEST)
#     return render(request , 'upload_doc.html')

# def uploadimage(request):
#     if not request.session.has_key("uid"):
#         return redirect("/accounts/login")
#     if request.method == "POST":
#         uuid = request.session['uid']
        
#         if request.FILES:
#             Pancard = request.FILES['Pancard']
#             Aadhaarcard = request.FILES['Aadhaarcard']
#             Companyid = request.FILES['Companyid']
#             Photo = request.FILES['Photo']
#             print(Pancard.name)
#             data = {"uid":uuid ,"Pancard":Pancard.file.read() ,"Aadhaarcard":Aadhaarcard.file.read(),
#             "Companyid":Companyid.file.read(),"Photo":Photo.file.read(), "Pancard_file":Pancard.name,
#             "Aadhaarcard_file":Aadhaarcard.name,"Companyid_file":Companyid.name,
#             "Photo_file":Photo.name}
            
#             dbuid = Validate_user_detail(uuid)

#             if dbuid is not None and dbuid == uuid:
#                 Update_upload_doc(data)
#             else: 
#                 Insert_upload_doc(data)

#     return render(request , 'upload_doc.html')
    