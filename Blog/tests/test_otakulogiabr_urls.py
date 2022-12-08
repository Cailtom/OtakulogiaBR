from django.test import TestCase
from django.urls import reverse


class OtakulogiabrURLsTest(TestCase):
    def test_otakulogia_home_url_is_Ok(self):
        url = reverse('otakulogiabr:otakulogiabr')
        self.assertEqual(url, '/')

    def test_otakulogia_home_returns_status_code_is_200(self):
        response = self.client.get(reverse('otakulogiabr:otakulogiabr'))
        self.assertEqual(
            response.status_code, 200
        )
