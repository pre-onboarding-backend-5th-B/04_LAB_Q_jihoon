from rest_framework import serializers
from apiserver.models import SeoulGu

class SeoulGuSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeoulGu
        fields = ["id", "name"]