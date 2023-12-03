from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="test_check",
            password="Testuser123",
            year_of_experience="3",
        )

    def test_cook_year_of_experience_listed(self):
        """
        Test thant driver's license_number is in list_display on admin page
        :return:
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.year_of_experience)

    def test_cook_detail_year_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.year_of_experience)

    def test_driver_additional_detail_license_number_listed(self):
        """
        Test thant driver's license_number
        is in on admin additional detail page
        :return:
        """
        url = reverse("admin:kitchen_cook_add")
        res = self.client.get(url)
        self.assertTrue(res, self.cook.year_of_experience)
