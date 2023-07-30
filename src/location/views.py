from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import (
    ContourSerializer,
    DistrictSerializer,
    RegionSerializer,
    CantonSerializer,
)

from .services import RegionService, ContourService, CantonService, DistrictService


class ContourListView(generics.ListAPIView):
    serializer_class = ContourSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("canton__district", "canton__district__region")

    def get_queryset(self):
        return ContourService.get_list(is_deleted=False)


class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return DistrictService.get_list(is_deleted=False)


class CantonListView(generics.ListAPIView):
    serializer_class = CantonSerializer

    def get_queryset(self):
        return CantonService.get_list(is_deleted=False)


class RegionListView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        return RegionService.get_list(is_deleted=False)
