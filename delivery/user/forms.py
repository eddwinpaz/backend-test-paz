from django.forms import ModelForm
from user.models import User


class AuthForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]


class CreateForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "phone", "email", "password"]
