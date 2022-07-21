from django.db import models
from apps.notebook.models import Color
from djmoney.models.fields import MoneyField

class Type(models.Model):
    type = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.type


class Bag(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='things', blank=True, null=True )
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,blank=True, null=True)
    material = models.CharField(max_length=30)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
