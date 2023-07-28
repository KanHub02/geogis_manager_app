from django.contrib.gis.db import models

from common.models import GeoBaseModel


class Region(GeoBaseModel):
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название"
    )

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self) -> str:
        return self.title


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

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"

    def __str__(self) -> str:
        return self.title


class Canton(GeoBaseModel):
    district = models.ForeignKey(
        "location.District",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Район",
    )
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название"
    )

    class Meta:
        verbose_name = "Кантон"
        verbose_name_plural = "Кантоны"

    def __str__(self) -> str:
        return self.title


class Contour(GeoBaseModel):
    canton = models.ForeignKey(
        "location.Canton",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Кантон",
    )

    class Meta:
        verbose_name = "Контур"
        verbose_name_plural = "Контуры"
