import json
from rest_framework import status, permissions
from rest_framework import generics
from django.conf import settings
from rest_framework.decorators import api_view
from user_mgnts.models import *
from user_mgnts.serialize import *
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import render
import os
import boto3
from dotenv import load_dotenv
from rest_framework.schemas import AutoSchema
load_dotenv()


class GetDataView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        print(request.user.UserId)
        received_data = json.loads(request.body.decode('utf-8'))
        # print('RE',received_data)
        return JsonResponse(received_data)


class sign_up(generics.CreateAPIView):
    serializer_class = CognitoUserSerialize

    def post(self, request):
        user_data = JSONParser().parse(request)
        CognitoUserSerializer = CognitoUserSerialize(data=user_data)
        if CognitoUserSerializer.is_valid():
            client = boto3.client(
                'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
            response = client.sign_up(
                ClientId=settings.COGNITO_USER_CLIENT_ID,
                Username=CognitoUserSerializer.data['Email'],
                Password=CognitoUserSerializer.data['Password']
            )
            return JsonResponse((response), safe=False)


class confirm_sign_up(generics.CreateAPIView):
    serializer_class = ConfirmSignupSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            ConfirmSignupSerializer = ConfirmSignupSerialize(data=user_data)
            if ConfirmSignupSerializer.is_valid():
                print(ConfirmSignupSerializer.data['confirm_code'])
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.confirm_sign_up(
                    ClientId=settings.COGNITO_USER_CLIENT_ID,
                    Username=ConfirmSignupSerializer.data['Email'],
                    ConfirmationCode=ConfirmSignupSerializer.data['confirm_code']
                )

            return JsonResponse((response), safe=False)


class resend_confirm_code(generics.CreateAPIView):
    serializer_class = ResendConfirmcodeSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            ResendConfirmcodeSerializer = ResendConfirmcodeSerialize(
                data=user_data)
            if ResendConfirmcodeSerializer.is_valid():
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.resend_confirmation_code(
                    ClientId=settings.COGNITO_USER_CLIENT_ID,
                    Username=ResendConfirmcodeSerializer.data['Email']
                )

            return JsonResponse((response), safe=False)


class sign_in(generics.CreateAPIView):
    serializer_class = SigninSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            SigninSerializer = SigninSerialize(data=user_data)
            if SigninSerializer.is_valid():
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.initiate_auth(
                    ClientId=settings.COGNITO_USER_CLIENT_ID,
                    AuthFlow='USER_PASSWORD_AUTH',
                    AuthParameters={
                        'USERNAME': SigninSerializer.data['Email'],
                        'PASSWORD': SigninSerializer.data['Password']
                    }
                )

            return JsonResponse(response, safe=False)


class get_user(generics.CreateAPIView):
    serializer_class = GetUserSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            GetUserSerializer = GetUserSerialize(data=user_data)
            if GetUserSerializer.is_valid():

                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.get_user(
                    AccessToken=GetUserSerializer.data['AccessToken']
                )

            attr_sub = None
            for attr in response['UserAttributes']:
                if attr['Name'] == 'sub':
                    attr_sub = attr['Value']
                    break
            return JsonResponse((response), safe=False)


class confirm_forgot_password(generics.CreateAPIView):
    serializer_class = ConfirmForgotPasswordSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            ConfirmForgotPasswordSerializer = ConfirmForgotPasswordSerialize(
                data=user_data)
            if ConfirmForgotPasswordSerializer.is_valid():
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.confirm_forgot_password(
                    ClientId=settings.COGNITO_USER_CLIENT_ID,
                    Username=ConfirmForgotPasswordSerializer.data['Email'],
                    ConfirmationCode=ConfirmForgotPasswordSerializer.data['confirm_code'],
                    Password=ConfirmForgotPasswordSerializer.data['Password']
                )

            return JsonResponse((response), safe=False)


class forgot_password(generics.CreateAPIView):
    serializer_class = ForgotPasswordSerialize

    def post(self, request):
        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            ForgotPasswordSerializer = ForgotPasswordSerialize(data=user_data)
            if ForgotPasswordSerializer.is_valid():
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.forgot_password(
                    ClientId=settings.COGNITO_USER_CLIENT_ID,
                    Username=ForgotPasswordSerializer.data['Email']
                )

            return JsonResponse((response), safe=False)


class change_password(generics.CreateAPIView):
    serializer_class = ChangePasswordSerialize

    def post(self, request):

        if request.method == 'POST':
            user_data = JSONParser().parse(request)
            ChangePasswordSerializer = ChangePasswordSerialize(data=user_data)
            if ChangePasswordSerializer.is_valid():
                client = boto3.client(
                    'cognito-idp', region_name=settings.COGNITO_REGION_NAME)
                response = client.change_password(
                    PreviousPassword=ChangePasswordSerializer.data['PreviousPassword'],
                    ProposedPassword=ChangePasswordSerializer.data['NewPassword'],
                    AccessToken=ChangePasswordSerializer.data['AccessToken']
                )

            return JsonResponse((response), safe=False)
