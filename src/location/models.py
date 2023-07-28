from django.contrib.gis.db import models

from common.models import GeoBaseModel


class Region(GeoBaseModel):
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название"
    )


class District(GeoBaseModel):
    region = models.ForeignKey(
        "location.Region",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Регион",
    )
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название"
    )


class Canton(GeoBaseModel):
    district = models.ForeignKey(
        "location.District",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Район",
    )
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название"
    )


class Contour(GeoBaseModel):
    canton = models.ForeignKey(
        "location.Canton",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Кантон",
    )
