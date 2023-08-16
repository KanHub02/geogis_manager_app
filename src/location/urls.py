from django.urls import path

from .views import (
    ContourListView,
    CantonListView,
    RegionListView,
    DistrictListView,
    CreateGeometryApiView,
)


urlpatterns = [
    path("v1/contours/", ContourListView.as_view(), name="contour-list"),
    path("v1/regions/", RegionListView.as_view(), name="region-list"),
    path("v1/cantons/", CantonListView.as_view(), name="canton-list"),
    path("v1/districts/", DistrictListView.as_view(), name="disctrict-list"),
    path(
        "v1/create/",
        CreateGeometryApiView.as_view(),
    ),
]
