from rest_framework import serializers
from BarvaAPI.Models.Order_ticketdetailsModels import Order_ticketdetailsModel

class Order_ticketdetailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Order_ticketdetailsModel
        fields = "__all__"