from typing import Union, List, Any, Dict


from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from location.models import Region, District, Canton, Contour

import json
from geojson import Polygon


class GetGeoDataCommandMixin:
    _model_region = Region
    _model_disctrict = District
    _model_canton = Canton
    _model_contour = Contour


    def _create_district(self, region_title: str, step: int):
            region = self._model_region.objects.filter(title=region_title).first()
            if region:
                with open("./kgz_disctricts.geojson", "r") as data:
                    data_text = data.read()
                    data_json = json.loads(data_text)
                    title = data_json.get("features")[step]["properties"].get("name_2")
                    polygon = data_json.get("features")[step]["geometry"]
                    polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                    self._model_disctrict.objects.create(title=title, region=region, geometry=polygon_wkb)


    def get_data_execute(self):
        with open("./kgz_regions.geojson", "r") as data:
            data_text = data.read()
            data_json = json.loads(data_text)
            len_of_regions = len(data_json.get("features"))
            step = 0
            for region in range(len_of_regions):
                step += 1
                polygon = data_json.get("features")[region]["geometry"]
                region_title = data_json.get("features")[region]["properties"].get("name")
                polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                self._model_region.objects.get_or_create(
                    title=region_title, geometry=polygon_wkb
                )
                self._create_district(region_title=region_title, step=step)


class Command(BaseCommand, GetGeoDataCommandMixin):
    def handle(self, *args: Any, **options: Any):
        return self.get_data_execute()
