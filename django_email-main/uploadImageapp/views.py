from django.shortcuts import render,redirect
from register_details.models import Register_details
from rest_framework.views import APIView
from rest_framework.response import Response
from uploadImageapp.serialize import UploadSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from uploadImageapp.databaseProvider.upload_documentsCRUD import *

@api_view(['POST'])
def index(request):
    if request.method == "POST":
        saveserialize = UploadSerialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data,status=status.HTTP_201_CREATED)
            return Response(saveserialize.data , status = status.HTTP_400_BAD_REQUEST)
    return render(request , 'upload_doc.html')

def uploadimage(request):
    if not request.session.has_key("uid"):
        return redirect("/accounts/login")
    if request.method == "POST":
        uuid = request.session['uid']
        
        if request.FILES:
            Pancard = request.FILES['Pancard']
            Aadhaarcard = request.FILES['Aadhaarcard']
            Companyid = request.FILES['Companyid']
            Photo = request.FILES['Photo']
            print(Pancard.name)
            data = {"uid":uuid ,"Pancard":Pancard.file.read() ,"Aadhaarcard":Aadhaarcard.file.read(),
            "Companyid":Companyid.file.read(),"Photo":Photo.file.read(), "Pancard_file":Pancard.name,
            "Aadhaarcard_file":Aadhaarcard.name,"Companyid_file":Companyid.name,
            "Photo_file":Photo.name}
            
            dbuid = Validate_user_detail(uuid)

            if dbuid is not None and dbuid == uuid:
                Update_upload_doc(data)
            else: 
                Insert_upload_doc(data)

    return render(request , 'upload_doc.html')
    