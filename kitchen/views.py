import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, CookCreationForm, CookExperienceUpdateForm, DishTypeSearchForm, CookSearchForm
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


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return DishType.objects.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return DishType


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type_form"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type_form"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    fields = "__all__"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        first_name = self.request.GET.get("first_name", "")
        context["search_form"] = CookSearchForm(
            initial={"first_name": first_name}
        )
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return Cook.objects.filter(
                first_name__icontains=form.cleaned_data["first_name"]
            )
        return Cook


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


def logout_view(request):
    logout(request)
    return render(request, "logged_out.html")
