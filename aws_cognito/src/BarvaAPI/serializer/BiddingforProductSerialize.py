from rest_framework import serializers
from BarvaAPI.Models.BiddingforProductModels import BidProductModel,BidCalModel

class BidProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = BidProductModel
        fields = "__all__"
        
class BidCalSerialize(serializers.ModelSerializer):
    class Meta:
        model = BidCalModel
        fields = "__all__"