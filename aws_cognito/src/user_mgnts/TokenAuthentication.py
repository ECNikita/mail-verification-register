from rest_framework import authentication, exceptions
from django.conf import settings
from user_mgnts.models import *
from django.contrib.auth.models import User
import  boto3

class TokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        
        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            print(token)
            client = boto3.client('cognito-idp', region_name=settings.COGNITO_REGION_NAME)
            response = client.get_user(AccessToken= token)
            print(response)

            user = UserIdModel
            for attr in response['UserAttributes']:
                if attr['Name'] == 'sub':
                    user.UserId = attr['Value']
                    break
            
            return (user, token)

        except:
            print('Error')
            raise exceptions.AuthenticationFailed('Your token is invalid,login')
        

        return super().authenticate(request)