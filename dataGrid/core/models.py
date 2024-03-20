from django.db import models

# Create your models here.

class Bus(models.Model):
    name = models.CharField( max_length=50)
    color = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    