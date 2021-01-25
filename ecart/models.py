from django.db import models

# Create your models here.
class Materials(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField
    price = models.IntegerField(default=0)
    