from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUser


class custom_register_user_form(UserCreationForm):
    class Meta:
        model = customUser
        # fields = ["name"]
        fields = ["age"]


class custom_change_user_form(UserChangeForm):
    password = None

    class Meta:
        model = customUser
        # fields = ["name"]
        fields = ["age"]
