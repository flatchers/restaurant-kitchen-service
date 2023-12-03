from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Hot Snack")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish(self):
        dish = Dish.objects.create()