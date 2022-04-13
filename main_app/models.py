from django.db import models

# Create your models here.
class Fish(models.Model):
    kind = models.CharField(max_length=50)
    length = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.kind