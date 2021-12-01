from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
