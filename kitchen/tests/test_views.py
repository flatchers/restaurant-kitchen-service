from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.forms import CookCreationForm, CookExperienceUpdateForm, ExperienceForm
from kitchen.models import Cook, Dish, DishType

DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")
DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicDishTest(TestCase):
    def test_dish_required(self):
        res = self.client.get(DISH_URL)
        self.assertEqual(res.status_code, 200)


class PublicCookTest(TestCase):
    def test_cook_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test12345",
        )
        self.client.force_login(self.user)

    def test_cook_retrieve(self):
        Cook.objects.create(
            username="test1.test",
            first_name="test1",
            password="Test12345",
            year_of_experience=2,
        )
        Cook.objects.create(
            username="test2.test",
            first_name="test2",
            password="Test12342",
            year_of_experience=3,
        )
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)


class PublicDishTypeTest(TestCase):
    def test_dish_type_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertEqual(res.status_code, 200)
