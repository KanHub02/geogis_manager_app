from typing import Union, List, Any, Dict

import logging

from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand
from location.models import Region, District, Canton, Contour

import json

from .utils import GetGeoDataExtra


class GetGeoDataCommandMixin(GetGeoDataExtra):
    def _create_one_region(self):
        try:
            with open("./kgz_regions.geojson", "r") as data:
                data_text = data.read()
                data_json = json.loads(data_text)
                region_title = data_json.get("features")[2]["properties"].get("name")
                polygon = data_json.get("features")[2]["geometry"]
                polygon_wbt = self._polygon_converter(polygon)
                self._model_region.objects.get_or_create(
                    title=region_title, geometry=polygon_wbt
                )

        except Exception as e:
            logging.error(e)

    def _three_districts(self):
        try:
            with open("./kgz_disctricts.geojson", "r") as data:
                data_json = json.load(data)

                region = self._model_region.objects.filter(title="Chuy").first()
                if region:
                    district_data = [
                        {
                            "index": 4,
                            "title": data_json["features"][4]["properties"].get(
                                "name_2"
                            ),
                            "geometry": data_json["features"][4]["geometry"],
                        },
                        {
                            "index": 7,
                            "title": data_json["features"][7]["properties"].get(
                                "name_2"
                            ),
                            "geometry": data_json["features"][7]["geometry"],
                        },
                        {
                            "index": 8,
                            "title": data_json["features"][8]["properties"].get(
                                "name_2"
                            ),
                            "geometry": data_json["features"][8]["geometry"],
                        },
                    ]

                    for district_info in district_data:
                        title = district_info["title"]
                        geometry = district_info["geometry"]
                        district = self._model_disctrict(title=title).DoesNotExist()
                        if not district:
                            self._model_disctrict.objects.get_or_create(
                                title=title,
                                region=region,
                                geometry=self._polygon_converter(geometry),
                            )
                        continue
        except Exception as e:
            logging.error(e)

    def get_data_execute(self):
        self._create_one_region()
        self._three_districts()


class Command(BaseCommand, GetGeoDataCommandMixin):
    def handle(self, *args: Any, **options: Any):
        return self.get_data_execute()
