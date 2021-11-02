from rest_framework import serializers
from BarvaAPI.Models.TraderroleModels import TraderroleModel

class TraderroleSerialize(serializers.ModelSerializer):
    class Meta:
        model = TraderroleModel
        fields = "__all__"