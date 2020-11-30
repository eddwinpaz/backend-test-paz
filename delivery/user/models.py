from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    admin = models.BooleanField(default=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.name
