from rest_framework import serializers
from user_mgnts.models import *


class CognitoUserSerialize(serializers.ModelSerializer):
    class Meta:
        model = CognitoUserModel
        fields ="__all__"

class UserIdSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserIdModel
        fields ="__all__"

class SigninSerialize(serializers.ModelSerializer):
    class Meta:
        model = SigninModel
        fields ="__all__"

class ConfirmSignupSerialize(serializers.ModelSerializer):
    class Meta:
        model = ConfirmSignupModel
        fields = "__all__"


class ResendConfirmcodeSerialize(serializers.ModelSerializer):
    class Meta:
        model = ResendConfirmcodeModel
        fields = "__all__"

class ForgotPasswordSerialize(serializers.ModelSerializer):
    class Meta:
        model = ForgotPasswordModel
        fields = "__all__"

class GetUserSerialize(serializers.ModelSerializer):
    class Meta:
        model = GetUserModel
        fields = "__all__"


class ConfirmForgotPasswordSerialize(serializers.ModelSerializer):
    class Meta:
        model = ConfirmForgotPasswordModel
        fields = "__all__"


class ChangePasswordSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChangePasswordModel
        fields = "__all__"
