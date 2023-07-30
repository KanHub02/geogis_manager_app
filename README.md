Django проект на основе тестового задания

git clone https://github.com/KanHub02/geo_management_app.git

Перейдите в папку проекта:

cd geo_management_app

Соберите и запустите контейнеры Docker с помощью команды:

docker-compose up --build

Для создания админа пользователя:

docker ps
docker exec -it <id_контейнера> python3 src/manage.py create_admin
username: admin
password: adminadmin

Для создания данных по типу:
информацией о одном регионе Кыргызстана, включающем в себя 3 района. Каждый район должен содержать по 2 айыльного округа.
docker exec -it <id_контейнера> python3 src/manage.py generate_geo_data

Откройте веб-браузер и перейдите по адресу http://0.0.0.0:1111/admin/ для доступа к AdminPanel приложения.

Откройте веб-браузер и перейдите по адресу http://0.0.0.0:1111/api/v1/docs/ для доступа к API документации приложения.


Настройка

Все настройки Django проекта находятся в файле settings.py в папке src/core/

Структура проекта

src/: Каталог с исходным кодом Django проекта.

entrypoints/: Каталог с sh скриптами

geojson/: Данные о территории Кыргызстана в формате GeoJson

Dockerfile: Файл Dockerfile для сборки образа Django приложения.

docker-compose.yml: Файл для настройки и запуска контейнеров Docker.