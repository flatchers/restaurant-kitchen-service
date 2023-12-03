from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.forms import CookCreationForm, CookExperienceUpdateForm, ExperienceForm
from kitchen.models import Cook, Dish, DishType


class FormsTest(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)

    def test_cook_isvalid(self):
        form_data = {
            "username": "test_check",
            "first_name": "first",
            "last_name": "second",
            "password1": "Test12345",
            "password2": "Test12345",
            "year_of_experience": 4,
        }

        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def validate_experience(self):
        form_data = {
            "year_of_experience": 4
        }
        invalid_form_data = {
            "year_of_experience": 43
        }
        form = ExperienceForm(data=form_data)
        form2 = ExperienceForm(data=invalid_form_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form2.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_search_form_by_username(self):
        Cook.objects.create_user(
            username="test1.test",
            first_name="test1",
            password="Test12345",
            year_of_experience=2,
        )
        Cook.objects.create_user(
            username="test2.test",
            first_name="test2",
            password="Test12342",
            year_of_experience=3,
        )
        response = self.client.get(
            reverse("kitchen:cook-list"),
            {"first_name": "test1"}
        )
        cooks = Cook.objects.filter(first_name__icontains="test1")
        print("response", response)
        self.assertEqual(list(response.context["cook_list"]), list(cooks))

    def test_dish_type_search_form_by_name(self):
        DishType.objects.create(
            name="test1"
        )
        DishType.objects.create(
            name="test2"
        )
        response = self.client.get(
            reverse("kitchen:dish-list"),
            {"name": "test1"}
        )
        dish = DishType.objects.filter(name__icontains="test1")
        print("response", response)
        self.assertEqual(list(response.context["dish_list"]), list(dish))
