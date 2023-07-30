from django.db.models import QuerySet

from abc import ABC, abstractmethod

from .models import Region, Canton, Contour, District


class AbstractSerice(ABC):
    _model = None

    @abstractmethod
    def get_list(cls) -> QuerySet[_model]:
        """Filtering django model and return queryset"""
        raise NotImplementedError


class DistrictService(AbstractSerice):
    _model = District

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )


class ContourService(AbstractSerice):
    _model = Contour

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "geometry")
        )


class CantonService(AbstractSerice):
    _model = Canton

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )


class RegionService(AbstractSerice):
    _model = Region

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )
