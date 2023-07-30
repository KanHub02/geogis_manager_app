from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Contour, Region, Canton, District


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
