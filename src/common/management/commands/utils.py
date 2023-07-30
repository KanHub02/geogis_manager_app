from typing import Union, List, Any, Dict

import logging

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from location.models import Region, District, Canton, Contour

import json
from geojson import Polygon


class GetGeoDataExtra:
    _model_region = Region
    _model_disctrict = District
    _model_canton = Canton
    _model_contour = Contour

    def _polygon_converter(self, polygon) -> GEOSGeometry:
        polygon_wtb = GEOSGeometry(json.dumps(polygon), srid=4326)
        return polygon_wtb

    def _create_all_district(self, region_title: str):
        with open("./kgz_disctricts.geojson", "r") as data:
            data_text = data.read()
            data_json = json.loads(data_text)
            len_of_disctricts = len(data_json.get("features"))
            for district in range(len_of_disctricts):
                type_of = data_json.get("features")[district]["properties"].get(
                    "type_2"
                )
                if type_of == "Rayon":
                    polygon = data_json.get("features")[district]["geometry"]
                    region_title = data_json.get("features")[district][
                        "properties"
                    ].get("name_1")
                    title = data_json.get("features")[district]["properties"].get(
                        "name_2"
                    )
                    region = self._model_region.objects.filter(
                        title__iconta=region_title[1::]
                    ).first()
                    if region:
                        district = self._model_disctrict.objects.filter(
                            title=title
                        ).exists()
                        if district:
                            continue
                        polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                        self._model_disctrict.objects.get_or_create(
                            title=title, region=region, geometry=polygon_wkb
                        )
                    else:
                        continue
                else:
                    continue

    def create_all_regions(self):
        with open("./kgz_regions.geojson", "r") as data:
            data_text = data.read()
            data_json = json.loads(data_text)
            len_of_regions = len(data_json.get("features"))
            step = 0
            for region in range(len_of_regions):
                step += 1
                polygon = data_json.get("features")[region]["geometry"]
                region_title = data_json.get("features")[region]["properties"].get(
                    "name"
                )
                polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                self._model_region.objects.get_or_create(
                    title=region_title, geometry=polygon_wkb
                )
