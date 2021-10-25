from rest_framework import serializers
from trade_details.models import Trade_detailsModel

class Trade_detailsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Trade_detailsModel
        fields = "__all__"