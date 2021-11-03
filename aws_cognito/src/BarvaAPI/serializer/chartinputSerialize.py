from rest_framework import serializers
from BarvaAPI.Models.chartinputModels import ChartModel,ChartResponseModel

class ChartSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChartModel
        fields = "__all__"

class ChartResponseSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChartResponseModel
        fields = "__all__"
