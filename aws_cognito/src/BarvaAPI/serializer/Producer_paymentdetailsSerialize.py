from rest_framework import serializers
from BarvaAPI.Models.Producer_paymentdetailsModels import Producer_paymentdetailsModel

class Producer_paymentdetailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Producer_paymentdetailsModel
        fields = "__all__"