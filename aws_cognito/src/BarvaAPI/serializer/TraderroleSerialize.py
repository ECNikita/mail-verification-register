from rest_framework import serializers
from BarvaAPI.Models.TraderroleModels import Traderrole_Model

class TraderroleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Traderrole_Model
        fields = "__all__"