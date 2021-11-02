from rest_framework import serializers
from BarvaAPI.Models.Trader_detailsModels import Trader_detailsModel

class Trader_detailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Trader_detailsModel
        fields = "__all__"