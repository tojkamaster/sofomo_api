from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, validate_ipv46_address
from rest_framework import serializers

from geo_api.models import GeoData


class GeoAddSerializer(serializers.Serializer):
    ip_or_url = serializers.CharField()


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = '__all__'
