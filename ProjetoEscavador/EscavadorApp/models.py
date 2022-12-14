from django.db import models

# Create your models here.
class Fontes(models.Model):
    id = models.AutoField(primary_key=True)
    fonte = models.CharField(max_length=250)

    def __str__(self):
        return self.fonte