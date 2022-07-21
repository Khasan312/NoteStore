from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model

User= get_user_model()

class CPU(models.Model):
    cpu = models.CharField(max_length=40)


    def __str__(self) -> str:
        return self.cpu

class Condition(models.Model):
    condition = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.condition

class Core(models.Model):
    core = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.core

class GPU(models.Model):
    gpu = models.CharField(max_length=60)


    def __str__(self) -> str:
        return self.gpu



class Storage(models.Model):
    storage = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.storage

class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.color



class Purpose(models.Model):
    purpose = models.CharField(max_length=50)
 
    def __str__(self) -> str:
        return self.purpose

class Brand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.brand

class NoteBook(models.Model):
   
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    desc = models.TextField()
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, blank=True, null=True)
    core_quantity = models.ForeignKey(Core, on_delete=models.CASCADE, blank=True, null=True)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, blank=True, null=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, blank=True, null=True)
    storage_device = models.ForeignKey(Storage, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title




