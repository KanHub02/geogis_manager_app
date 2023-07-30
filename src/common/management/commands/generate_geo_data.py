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

    def _generate_geo_json(self, list_of_polygons: List[List[List[float]]]) -> Dict:
            geo_json_data: Dict = {
                "geometry": {
                    "type": "Polygon",
                    "coordinates":[[[ 71.043091, 40.287865 ], [ 71.063042, 40.289806 ], [ 71.080452, 40.297779 ]]],
                }
            }
            print(geo_json_data)
            return geo_json_data


    def _split_region(self, input_list: List[List[List[int]]]) -> List[List[int]]:
        input_list = input_list[0]
        len_of_list = len(input_list)
        part_size = len_of_list // 3
        part1, part2, part3 = (
            input_list[:part_size],
            input_list[part_size : 2 * part_size],
            input_list[2 * part_size :],
        )
        list_of_parts = [part1, part2, part3]
        return list_of_parts

    def _create_district(
        self, region_title: str, split_range: int, list_of_parts: List[List[int]]
    ) -> None:
        step = 0
        region = self._model_region.objects.filter(title=region_title).first()
        data = self._generate_geo_json(list_of_parts[0])
        if region is not None:
            for _ in range(split_range):
                step += 1
                if step == 1:
                    data = self._generate_geo_json(list_of_parts[0])
                    polygon = data.get("geometry")
                    # print(json.dumps(polygon))
                    polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                    self._model_disctrict.objects.create(
                        region=region,
                        title=f"District of {region_title} #{_}",
                        geometry=polygon_wkb,
                    )
                # elif step == 2:
                #     data = self._generate_geo_json(list_of_parts[1])
                #     polygon = data.get("geometry")
                #     polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                #     self._model_disctrict.objects.create(
                #         region=region,
                #         title=f"District of {region_title} #{_}",
                #         geometry=polygon_wkb,
                #     )
                # elif step == 3:
                #     data = self._generate_geo_json(list_of_parts[2])
                #     polygon = data.get("geometry")
                #     polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                #     self._model_disctrict.objects.create(
                #         region=region,
                #         title=f"District of {region_title} #{_}",
                #         geometry=polygon_wkb,
                #     )

    def get_data_execute(self):
        with open("./kgz_regions.geojson", "r") as data:
            data_text = data.read()
            data_json = json.loads(data_text)
            len_of_regions = len(data_json.get("features"))
            for region in range(len_of_regions):
                polygon = data_json.get("features")[region]["geometry"]
                name = data_json.get("features")[region]["properties"].get("name")
                polygon_wkb = GEOSGeometry(json.dumps(polygon), srid=4326)
                self._model_region.objects.get_or_create(
                    title=name, geometry=polygon_wkb
                )
                parts_of_region_polygons = self._split_region(
                    polygon.get("coordinates")
                )
                self._create_district(
                    region_title=name,
                    split_range=3,
                    list_of_parts=parts_of_region_polygons,
                )


class Command(BaseCommand, GetGeoDataCommandMixin):
    def handle(self, *args: Any, **options: Any):
        return self.get_data_execute()
