from rest_framework import serializers
from BarvaAPI.Models.Order_detailsModels import Order_detailsModel

class Order_detailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Order_detailsModel
        fields = "__all__"