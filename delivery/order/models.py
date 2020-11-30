from django.db import models
from menu.models import Menu
from user.models import User


STATUS_CHOICES = (
    ("1", "Pending"),
    ("2", "Prepearing"),
    ("3", "Delivering"),
    ("4", "Delivered"),
)


class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    customization = models.CharField(max_length=250, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    delivered_date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.menu.name
