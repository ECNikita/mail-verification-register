from rest_framework import serializers
from uploadImageapp.models import UploadModel

class UploadSerialize(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = "__all__"