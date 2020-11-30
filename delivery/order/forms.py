from django.forms import ModelForm
from order.models import Order


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ["customization"]
