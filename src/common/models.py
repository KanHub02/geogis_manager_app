import uuid

from django.contrib.gis.db import models


class BaseModel(models.Model):
    """BaseModel is the base class that provides the basis for creating various models in our application."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    is_deleted = models.BooleanField(default=False, verbose_name="Удален")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class GeoBaseModel(BaseModel):
    """Base model for models is using PolygonField"""

    geometry = models.PolygonField(
        null=False, blank=False, verbose_name="Геомотрия", geography=True
    )

    class Meta:
        abstract = True
