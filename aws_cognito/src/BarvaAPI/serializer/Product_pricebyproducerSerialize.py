from rest_framework import serializers
from BarvaAPI.Models.Product_pricebyproducerModels import Product_pricebyproducerModel

class Product_pricebyproducerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product_pricebyproducerModel
        fields = "__all__"