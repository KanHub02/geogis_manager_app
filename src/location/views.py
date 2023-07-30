from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import (
    ContourSerializer,
    DistrictSerializer,
    RegionSerializer,
    CantonSerializer,
)

from .services import RegionService, ContourService, CantonService, DistrictService
from .schemas import ContourListSchema, CantonListSchema, DistrictListSchema, RegionListSchema


class ContourListView(generics.ListAPIView):
    """This class view filter(optional) and returns a list of Contour, according to all standards GeoJson"""
    serializer_class = ContourSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("canton__district", "canton__district__region")
    schema = ContourListSchema()

    def get_queryset(self):
        return ContourService.get_list(is_deleted=False)


class DistrictListView(generics.ListAPIView):
    """This class view returns a list of District, according to all standards GeoJson"""
    serializer_class = DistrictSerializer
    schema = DistrictListSchema()

    def get_queryset(self):
        return DistrictService.get_list(is_deleted=False)


class CantonListView(generics.ListAPIView):
    """This class view returns a list of Canton, according to all standards GeoJson"""
    serializer_class = CantonSerializer
    schema = CantonListSchema()

    def get_queryset(self):
        return CantonService.get_list(is_deleted=False)


class RegionListView(generics.ListAPIView):
    """This class view returns a list of Region, according to all standards GeoJson"""
    serializer_class = RegionSerializer
    schema = RegionListSchema()

    def get_queryset(self):
        return RegionService.get_list(is_deleted=False)
