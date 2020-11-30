from django.forms import ModelForm
from menu.models import Menu


class MenuAddForm(ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description", "expiration_date"]
