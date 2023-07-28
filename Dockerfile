FROM python:3.9-alpine

RUN mkdir -p /opt/services/geo-management

WORKDIR /opt/services/geo-management

ADD requirements.txt /opt/services/geo-management/

ADD . /opt/services/geo-management/

RUN apk add --no-cache gcc curl musl-dev linux-headers && \
        chmod 755 /opt/services/geo-management/entrypoints/* && \
            chmod +x /opt/services/geo-management/entrypoints/* && \
                pip install -r requirements.txt
                
RUN apk add --no-cache geos gdal
# RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing gdal-dev