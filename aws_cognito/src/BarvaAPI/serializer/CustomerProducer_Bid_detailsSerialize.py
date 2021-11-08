from rest_framework import serializers
from BarvaAPI.Models.CustomerProducer_Bid_detailsModels import CustomerProducer_Bid_detailsModel

class CustomerProducer_Bid_detailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = CustomerProducer_Bid_detailsModel
        fields = "__all__"