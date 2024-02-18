from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import custom_register_user_form, custom_change_user_form
from .models import customUser


class CustomUserAdmin(UserAdmin):
    add_form = custom_register_user_form
    form = custom_change_user_form
    model = customUser

    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]

    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)

    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(customUser, CustomUserAdmin)
