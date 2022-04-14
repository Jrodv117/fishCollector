from django.db import models
from django.urls import reverse
# Create your models here.
class Fish(models.Model):
    kind = models.CharField(max_length=50)
    length = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.kind

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})