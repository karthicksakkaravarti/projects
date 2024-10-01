from rest_framework import serializers
from projects.setup import models


class CriteriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Criteria
        fields = "__all__"


class CustomViewSerializers(serializers.ModelSerializer):
    criteria = CriteriaSerializers()

    class Meta:
        model = models.CustomView
        fields = "__all__"
