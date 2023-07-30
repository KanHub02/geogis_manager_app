from django.db.models import QuerySet

from .models import Region, Canton, Contour, District


class DistrictService:
    _model = District

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )


class ContourService:
    _model = Contour

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "geometry")
        )


class CantonService:
    _model = Canton

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )


class RegionService:
    _model = Region

    @classmethod
    def get_list(cls, **kwargs) -> QuerySet[_model]:
        return (
            cls._model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "geometry")
        )
