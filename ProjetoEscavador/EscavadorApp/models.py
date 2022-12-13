from django.db import models

# Create your models here.
class Fontes(models.Model):
    fonte = models.CharField(max_length=250)