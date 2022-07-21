from django.db import models
from django.contrib.auth import get_user_model

from apps.notebook.models import NoteBook

User = get_user_model()


class OrderItem(models.Model):
    product = models.OneToOneField(NoteBook, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.IntegerField(default=1)


    def __str__(self) -> str:
        return str(self.product)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=1)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(null=True)


    def __str__(self) -> str:
        return str(self.items)

    


