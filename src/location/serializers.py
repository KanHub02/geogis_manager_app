from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from rest_framework import serializers

from django.core.serializers import serialize

from .models import Contour, Region, Canton, District, GeoObject


class DistrictSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = District
        geo_field = "geometry"
        fields = ("id", "title")


class RegionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Region

        geo_field = "geometry"
        fields = ("id", "title")


class CantonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Canton
        geo_field = "geometry"
        fields = ("id", "title")


class ContourSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Contour
        geo_field = "geometry"
        fields = ("id",)        


class GeometryCreateSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeoObject
        geo_field = "geometry"
        fields = ("title",)    

        