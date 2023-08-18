import logging

from django.urls import reverse

from tests.base_case import BaseGeoApiTestCase

from location.models import Region, Canton, Contour, District


class LocationsTestCase(BaseGeoApiTestCase):
    def test_list_regions_status_code(self):
        response = self.client.get(reverse("region-list"))
        self.assertEqual(response.status_code, 200)

    def test_regions_id(self):
        response = self.client.get(reverse("region-list"))
        reponse_objects_id = response.json().get("features")[0].get("id")
        region = Region.objects.filter(id=reponse_objects_id).exists()
        self.assertTrue(region)

    def test_contour_list_status(self):
        response = self.client.get(reverse("contour-list"))
        self.assertEqual(response.status_code, 200)

    def test_contour_list(self):
        response = self.client.get(reverse("contour-list"))
        response_obj_id = response.json().get("features")[0].get("id")
        canton_id = Contour.objects.filter(id=response_obj_id).exists()
        self.assertTrue(canton_id)

    def test_cantons_status(self):
        response = self.client.get(reverse("canton-list"))
        self.assertEqual(response.status_code, 200)

    def test_cantons_list(self):
        response = self.client.get(reverse("canton-list"))
        response_obj_id = response.json().get("features")[0].get("id")
        canton_id = Canton.objects.filter(id=response_obj_id).exists()
        self.assertTrue(canton_id)

    def test_disctricts_status(self):
        response = self.client.get(reverse("disctrict-list"))
        self.assertEqual(response.status_code, 200)

    def test_district_list(self):
        response = self.client.get(reverse("disctrict-list"))
        response_obj_id = response.json().get("features")[0].get("id")
        district_id = District.objects.filter(id=response_obj_id).exists()
        self.assertTrue(district_id)
