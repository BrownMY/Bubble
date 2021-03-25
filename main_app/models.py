from django.db import models

# Create your models here.
class Waters(models.Model):
    brand = models.CharField(max_length=100)
    sizeoz = models.IntegerField()
    watertype = models.CharField(max_length=100)


def __str__(self):
    return self.name