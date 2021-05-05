import requests
from django.conf import settings


from rest_framework import status, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from geo_api.models import GeoData
from geo_api.serializers import GeoAddSerializer, GeoSerializer


class GeoAddView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = GeoData.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return GeoAddSerializer
        else:
            return GeoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ipstack_response = (
            requests.get(
                "http://api.ipstack.com/{}?access_key={}".format(
                    serializer.data.get('ip_or_url'),
                    settings.IPSTACK_ACCESS_KEY
                )
            )
            .json()
        )

        if not ipstack_response['type']:
            raise NotFound

        GeoData.objects.create(
            ip_or_url=serializer.data.get('ip_or_url'),
            ip=ipstack_response.get('ip'),
            country_name=ipstack_response.get('country_name'),
            city=ipstack_response.get('city'),
            latitude=ipstack_response.get('latitude'),
            longitude=ipstack_response.get('longitude'),
            created_at=ipstack_response.get('created_at')
        )

        return Response(status=status.HTTP_201_CREATED)