import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm
from kitchen.models import DishType, Cook, Dish


def index(request):
    """View function for the home page of the site."""

    num_dish_type = DishType.objects.count()
    num_cook = Cook.objects.count()
    num_dish = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dish_type": num_dish_type,
        "num_cook": num_cook,
        "num_dish": num_dish,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type_detail"


# class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
#     model = DishType
#     form_class = DishForm
#     success_url = reverse_lazy("taxi:car-list")

class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


# @login_required
# def toggle_assign_to_car(request, pk):
#     cook = Cook.objects.get(id=request.user.id)
#     if (
#         Car.objects.get(id=pk) in driver.cars.all()
#     ):  # probably could check if car exists
#         driver.cars.remove(pk)
#     else:
#         cook.cars.add(pk)
#     return HttpResponseRedirect(reverse_lazy("taxi:car-detail", args=[pk]))

