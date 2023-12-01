from django.urls import path

from kitchen.views import (
    index, DishTypeListView, CookListView, DishListView, CookDetailView, DishDetailView, DishTypeDetailView,
    DishUpdateView, DishCreateView, CookCreateView, CookUpdateView, DishTypeUpdateView, DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list",),
    path("dish-type/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail",),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish-type-create",),
    path("dish-type/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update",),
    path("cook/", CookListView.as_view(), name="cook-list",),
    path("cook/create/", CookCreateView.as_view(), name="cook-create",),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path(
        "cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list",),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail",),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("", index, name="index"),
    ]
app_name = "kitchen"
