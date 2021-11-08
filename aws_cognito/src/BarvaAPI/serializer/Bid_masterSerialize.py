from rest_framework import serializers
from BarvaAPI.Models.Bid_masterModels import Bid_masterModel

class Bid_masterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Bid_masterModel
        fields = "__all__"