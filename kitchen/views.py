import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from kitchen.models import DishType, Cook, Dish


@login_required
def index(request):
    """View function for the home page of the site."""

    num_dish_type = DishType.objects.count()
    num_cook = Cook.objects.count()
    num_dish = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_type ": num_dish_type,
        "num_num_cook": num_cook,
        "num_num_dish": num_dish,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)
