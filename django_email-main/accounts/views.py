import random
from accounts.models import Profile
from django.shortcuts import redirect, render
from accounts.databaseProvider.userCRUD import *
from django.contrib import messages
from rest_framework.parsers import JSONParser 
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serialize import AccountsSerialize
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = user_all()
        
        uids = request.query_params.get('uid', None)
        
        if uids is not None:
            for x in users:     
                if int(x.uid) == int(uids):
                    users=[x]
                    break

        AccountsSerializer = AccountsSerialize(users, many=True)
        return JsonResponse(AccountsSerializer.data, safe=False)


    elif request.method == 'POST':
        try:
            print("hello")
            user_data = json.loads(request.body)
            print(user_data)
            valid_user = Validate_user_detail(user_data["uid"])
            res = False
            
            if valid_user is not None and int(valid_user)==int(user_data["uid"]):
                res= user_update(user_data)
            else:
                otp= random.randint(10000,99999)
                res = user_insert(user_data,otp)
                send_mail_after_registration(user_data["Email"],otp)

            
            if res is True:
                data= {"res":"True"}
                return JsonResponse((data), safe=False)
            else :
                data= {"res":"False"}
                return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)
        except json.decoder.JSONDecodeError:
	        print("There was a problem accessing the equipment data.")

    elif request.method == 'DELETE':
        uid = request.query_params.get('uid', None)
        
        res=False
        res = user_delete(uid)

        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def activate_user(request):
    if request.method == 'POST':
        user_data = json.loads(request.body)
        print(user_data)
        valid_user = Verify_user(user_data["Email"],user_data["otp"])
        res = False
        if valid_user is True:
            res= Activate_user(user_data["Email"])
        
        if res is True:
            data= {"res":"True"}
            return JsonResponse((data), safe=False)
        else :
            data= {"res":"False"}
            return JsonResponse((data), status=status.HTTP_400_BAD_REQUEST)

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'please enter this otp on activation page : {token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    