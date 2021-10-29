from rest_framework import serializers
from BarvaAPI.Models.Product_masterModels import Product_masterModel

class Product_masterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product_masterModel
        fields = "__all__"