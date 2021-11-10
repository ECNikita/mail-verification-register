from rest_framework import serializers
from BarvaAPI.Models.WarehouseModels import WarehouseModel

class WarehouseSerialize(serializers.ModelSerializer):
    class Meta:
        model = WarehouseModel
        fields = "__all__"