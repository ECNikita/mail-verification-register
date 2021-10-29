from rest_framework import serializers
from BarvaAPI.Models.Lotunit_masterModels import Lotunit_masterModel

class Lotunit_masterSerialize(serializers.ModelSerializer):
    class Meta:
        model = Lotunit_masterModel
        fields = "__all__"