from typing import Union, List, Any

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from location.models import Region

import json


class GeoDataCommandMixin:
    _model = Region

    @classmethod
    def get_region(cls):
        with open("./kgz_regions.geojson", "r") as data:
            data_text = data.read()
            data_json = json.loads(data_text)
            len_of_regions = len(data_json.get("features"))
            for region in range(len_of_regions):
                polygon = data_json.get("features")[region]["geometry"]
                name = data_json.get("features")[region]["properties"].get("name")
                polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                cls._model.objects.create(title=name, geometry=polygon_wkb)


class Command(BaseCommand, GeoDataCommandMixin):
    def handle(self, *args: Any, **options: Any):
        return self.get_region()
