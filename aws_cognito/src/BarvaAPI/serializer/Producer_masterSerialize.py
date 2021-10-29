from rest_framework import serializers
from BarvaAPI.Models.Producer_masterModels import Producer_masterModel

class Producer_masterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Producer_masterModel
        fields = "__all__"