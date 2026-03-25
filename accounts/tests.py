from django.test import TestCase


class HomePageViewTests(TestCase):
    def test_root_url_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/home.html")
