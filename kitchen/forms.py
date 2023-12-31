from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, Cook


def validate_year_of_experience(year_of_experience):
    if year_of_experience > 42:
        raise ValidationError(
            "Selected age is unacceptable.We fire people after 60"
        )
    return year_of_experience


class ExperienceForm(forms.Form):
    year_of_experience = forms.IntegerField(validators=[validate_year_of_experience])


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "year_of_experience",
        )

    def clean_year_of_experience(self):  # this logic is optional, but possible
        return validate_year_of_experience(self.cleaned_data["year_of_experience"])


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["year_of_experience"]

    def clean_license_number(self):
        return validate_year_of_experience(self.cleaned_data["year_of_experience"])


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


class CookSearchForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
