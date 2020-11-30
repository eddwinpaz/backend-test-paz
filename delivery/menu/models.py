import uuid as uuid
from django.db import models


class Menu(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=250, null=True)
    expiration_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
