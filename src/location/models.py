from django.contrib.gis.db import models

from common.models import GeoBaseModel


class Region(GeoBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название",
        unique=True,
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
        related_name="districts",
    )
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название", unique=True
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
        related_name="cantons",
    )
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Название", unique=True
    )

    class Meta:
        verbose_name = "Округ"
        verbose_name_plural = "Округи"

    def __str__(self) -> str:
        return self.title


class Contour(GeoBaseModel):
    canton = models.ForeignKey(
        "location.Canton",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Кантон",
        related_name="contours",
    )

    class Meta:
        verbose_name = "Контур"
        verbose_name_plural = "Контуры"

    def __str__(self) -> str:
        return f"Контур {self.canton.title}"


class GeoObject(GeoBaseModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название",
        unique=True,
    )

    class Meta:
        verbose_name = "Обьект"
        verbose_name_plural = "Обьекты"
