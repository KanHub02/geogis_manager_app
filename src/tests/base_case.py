from rest_framework.test import APITestCase

from scripts.services import GeographyDataService


class BaseGeoApiTestCase(APITestCase):

    def setUp(self) -> None:
        service = GeographyDataService()
        return service.execute()

