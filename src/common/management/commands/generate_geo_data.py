from typing import Any

import json

import logging

from django.core.management.base import BaseCommand

from .utils import GetGeoDataExtra


class GetGeoDataCommandMixin(GetGeoDataExtra):

    def _create_two_cantons_for_jaiyl(self, path_to_geojson_file: str, district_title: str) -> None:
        district = self._model_disctrict.objects.filter(title=district_title).first()
        if not district:
            raise ValueError(f"District '{district_title}' not found.")
        
        with open(path_to_geojson_file, "r") as data:
            data_json = json.load(data)
            features = data_json.get("features", [])
            
            for feature in features:
                properties = feature.get("properties", {})
                title = properties.get("title")  
                geometry = feature.get("geometry")
                polygon_wtb = self._polygon_converter(geometry)
                self._model_canton.objects.create(title=title, geometry=polygon_wtb, district=district)

    def _create_one_region(self, path_to_geojson_file: str) -> None:
        try:
            with open(path_to_geojson_file, "r") as data:
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

    def _three_districts(self, path_to_geojson_file: str) -> None:
        try:
            with open(path_to_geojson_file, "r") as data:
                data_json = json.load(data)

                region = self._model_region.objects.filter(title="Chuy").first()
                if region:
                    district_data = [
                        {
                            "index": 4,
                            "title": data_json["features"][5]["properties"].get(
                                "name_2"
                            ),
                            "geometry": data_json["features"][5]["geometry"],
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
                        if district:
                            self._model_disctrict.objects.get_or_create(
                                title=title,
                                region=region,
                                geometry=self._polygon_converter(geometry),
                            )
                        continue
        except Exception as e:
            logging.error(e)

    def get_data_execute(self) -> None:
        self._create_one_region("./geojson/regions/kgz_regions.geojson")
        self._three_districts("./geojson/districts/kgz_disctricts.geojson")
        self._create_two_cantons_for_jaiyl(path_to_geojson_file="./geojson/cantons/jaiyldata.geojson", district_title="Jaiyl")
        self._create_two_cantons_for_jaiyl(path_to_geojson_file="./geojson/cantons/chuydata.geojson", district_title="Chui")
        self._create_two_cantons_for_jaiyl(path_to_geojson_file="./geojson/cantons/alamudun.geojson", district_title="Alamüdün")

        


class Command(BaseCommand, GetGeoDataCommandMixin):
    def handle(self, *args: Any, **options: Any):
        return self.get_data_execute()
