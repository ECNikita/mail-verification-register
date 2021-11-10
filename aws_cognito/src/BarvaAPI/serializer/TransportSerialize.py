from rest_framework import serializers
from BarvaAPI.Models.TransportModels import TransportModel

class TransportSerialize(serializers.ModelSerializer):
    class Meta:
        model = TransportModel
        fields = "__all__"