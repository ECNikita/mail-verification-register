from rest_framework import serializers
from BarvaAPI.Models.chartinputModels import ChartModel,ChartResponseModel,ChartResponseModel1

class ChartSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChartModel
        fields = "__all__"

class ChartResponseSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChartResponseModel
        fields = "__all__"

class ChartResponse1Serialize(serializers.ModelSerializer):
    class Meta:
        model = ChartResponseModel1
        fields = "__all__"