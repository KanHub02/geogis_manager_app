from typing import Any

from django.core.management.base import BaseCommand

from scripts.services import GeographyDataService


class Command(BaseCommand):
    def handle(self,  *args: Any, **options: Any):
        service = GeographyDataService()
        return service.get_data_execute()
