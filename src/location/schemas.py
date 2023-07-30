import coreapi
from rest_framework.schemas.coreapi import AutoSchema
import coreschema


class ContourListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        api_fields = []
        if method == "GET":
            api_fields = [
                coreapi.Field(
                    name="canton__district",
                    required=False,
                    location="query",
                    schema=coreschema.String(description="Use id field if need to filtering by district"),
                ),
                coreapi.Field(
                    name="canton__district__region",
                    required=False,
                    location="query",
                    schema=coreschema.String(description="Use id field if need to filtering by region "),
                ),
            ]
        return self._manual_fields + api_fields

class CantonListSchema(AutoSchema):
     def get_manual_fields(self, path, method):
        api_fields = []
        return self._manual_fields + api_fields


class DistrictListSchema(AutoSchema):
     def get_manual_fields(self, path, method):
        api_fields = []
        return self._manual_fields + api_fields


class RegionListSchema(AutoSchema):
     def get_manual_fields(self, path, method):
        api_fields = []
        return self._manual_fields + api_fields
     