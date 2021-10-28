from rest_framework import serializers
from BarvaAPI.Models.registerModels import Register_details

class RegistrateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Register_details
        fields = "__all__"