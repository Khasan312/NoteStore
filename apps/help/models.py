from django.db import models

class Help(models.Model):
    help = models.TextField()


    def __str__(self) -> str:
        return self.help


class AboutUs(models.Model):
    about_us = models.TextField()


    def __str__(self) -> str:
        return self.about_us

    class Meta:
        verbose_name_plural = ('About us')