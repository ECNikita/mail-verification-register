from rest_framework import serializers
from product_details.models import Product_detailsModel


class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Product_detailsModel
        fields = "__all__"
