from rest_framework import serializers
from BarvaAPI.Models.Producer_calculationModels import ProducerCalModel

class ProducerCalSerialize(serializers.ModelSerializer):
    class Meta:
        model = ProducerCalModel
        fields = "__all__"