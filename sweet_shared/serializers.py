from rest_framework import serializers

from sweet_shared.models import SweetType


class SweetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SweetType
        fields = ('name',)

