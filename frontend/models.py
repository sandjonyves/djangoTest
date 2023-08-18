from django.db import models


# Create your models here.
class DataReact(models.Model):
    name = models.CharField(max_length=200)
    niveau = models.CharField(max_length=100)
    classe = models.CharField(max_length=200)

    def __str__(self):
        return self.name