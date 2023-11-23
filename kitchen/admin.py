from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("year_of_experience", )
    fieldsets = UserAdmin.fieldsets + ((
                                           "Additional info", {"fields": ("year_of_experience", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name", "last_name",
                                                                               "year_of_experience", )}),)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", ]
    list_filter = ["name", ]
    search_fields = ["name", ]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    list_filter = ["name", ]
    search_fields = ["name", ]
