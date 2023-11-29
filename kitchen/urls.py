from django.urls import path

from kitchen.views import (
    index, DishTypeListView, CookListView, DishListView, CookDetailView, DishDetailView, DishTypeDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list",),
    path("dish-type/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail",),
    path("cook/", CookListView.as_view(), name="cook-list",),
    path(
        "cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list",),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail",),
    ]

app_name = "kitchen"
