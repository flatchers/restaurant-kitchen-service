from django.test import TestCase

from kitchen.models import DishType


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Hot Snack")
        self.assertEqual(str(dish_type), dish_type.name)
