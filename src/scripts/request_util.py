from sentinel2_downloader import SentinelAPI
from django.contrib.gis.geos import GEOSGeometry

import json
from datetime import datetime

from decouple import config as env


import requests
from decouple import config as env
from pprint import pprint

reponse_option = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name eq 'S2A_MSIL1C_20230816T055641_N0509_R091_T43TDH_20230816T083017.SAFE'"

username = env("DATASPACE_USERNAME")
password = env("DATASPACE_PASSWORD")

api = SentinelAPI(username=username, password=password)

access_token = api.token.get("access_token")

headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(reponse_option, allow_redirects=False)
response_data = json.loads(response.content)

end_date_data = response_data.get("value")[0].get("ContentDate").get("End")
start_date_data = response_data.get("value")[0].get("ContentDate").get("Start")

datetime_end_date_data = datetime.strptime(end_date_data, "%Y-%m-%dT%H:%M:%S.%fZ")
datetime_start_date_data = datetime.strptime(start_date_data, "%Y-%m-%dT%H:%M:%S.%fZ")

formatted_end_date_data = datetime_end_date_data.strftime("%Y-%m-%d")
formatted_start_date_data = datetime_start_date_data.strftime("%Y-%m-%d")

polygon_data = response_data.get("value")[0].get("GeoFootprint")
polygon_wtb = GEOSGeometry(json.dumps(polygon_data))

cleaned_polygon_wtb = str(polygon_wtb).replace("SRID=4326;", "")
# print(f"Polygon: \n{cleaned_polygon_wtb}\nstart_date: {formatted_start_date_data}\nend_data: {formatted_end_date_data}")


products = api.query(
    footprint=cleaned_polygon_wtb,
    start_date="2023-05-15",
    end_date="2023-05-16",
    cloud_cover_percentage="20",
    product_type="MSIL1C",
    platform_name="SENTINEL-2",
)

if len(products) > 1:
    a = api.download(product_id=products[0]["Id"], directory_path="output")
