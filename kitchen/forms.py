from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, Cook


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("username", "first_name", "last_name", "year_of_experience", "email", )

    def clean_year_of_experience(self):
        year_of_experience = self.cleaned_data["year_of_experience"]
        if year_of_experience > 42:
            raise ValidationError(
                "Selected age is unacceptable.We fire people after 60"
            )
        return year_of_experience


class CookCreationForm(UserCreationForm, CookExperienceUpdateForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "year_of_experience",
        )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
