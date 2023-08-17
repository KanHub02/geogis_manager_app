# import requests


# headers = {
#     "client_id": "96f31f46-0ce9-4ab0-96ba-a7b4fa428274",
#     "client_secret": "7spwyJQ9xHMdJT0VoMBKEaCxxn9iWdrX",

# }

# data = {
#     "bbox": [13, 45, 14, 46],
#     "datetime": "2019-12-10T00:00:00Z/2019-12-10T23:59:59Z",
#     "collections": ["sentinel-1-grd"],
#     "limit": 5,
#     "next": 5,
# }

# url = "https://dataspace.copernicus.eu/dss/odata/v1/Products('S2A_MSIL2A_20230816T055641_N0509_R091_T43TDG_20230816T110301.SAFE')/$value"
# response = requests.get(url, json=data, headers=headers)


# print(response.content)

# import requests
# import zipfile
# import io

# # Вставьте свой токен доступа (API key) сюда
# API_KEY = "YOUR_API_KEY"

# # Заголовки для авторизации с токеном доступа
# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# # Запрос на получение данных
# response = requests.get(url, headers=headers)

# zip_data = io.BytesIO(response.content)
# with zipfile.ZipFile(zip_data, "r") as zip_ref:
#         # Замените "output_folder" на путь к папке, куда вы хотите сохранить данные
#         output_folder = "path/to/output/folder"
#         zip_ref.extractall(output_folder)
# print("Shapefile успешно загружен и распакован!")

import requests
from decouple import config as env
from pprint import pprint

reponse_option = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name eq 'S2A_MSIL2A_20230816T055641_N0509_R091_T43TDH_20230816T110301.SAFE'")

access_token = env("DATASPACE_ACCESS_TOKEN")
session = requests.Session()
session.headers.update({'Authorization': f'Bearer {access_token}'})
url = f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products(c6c6c08e-7f98-44c1-9535-295b4ea8cf32)/$value"
response = session.get(url, allow_redirects=False)

while response.status_code in (301, 302, 303, 307):
    url = response.headers['Location']
    response = session.get(url, allow_redirects=False)

file = session.get(url, verify=False, allow_redirects=True)

with open(f"product.zip", 'wb') as p:
    p.write(file.content)