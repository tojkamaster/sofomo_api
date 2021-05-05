from django.db import models


class GeoData(models.Model):
    ip_or_url = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=False)
    country_name = models.CharField(null=False, max_length=100)
    city = models.CharField(null=False, max_length=100)

    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
