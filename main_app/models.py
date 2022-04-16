from django.db import models
from django.urls import reverse

BAITS = (
    ('LB', 'Live Bait'),
    ('L', 'Lure'),
    ('S', 'Spinner'),
    ('P', 'Power Bait'),
    ('SE', 'Salmon Eggs')
)

# Create your models here.

class Location(models.Model):
    name = models.CharField('Location Name', max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('locations_detail', kwargs={'pk': self.id})

class Fish(models.Model):
    kind = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.kind

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})

class Bait(models.Model):
    type = models.CharField(
        'Types Of Bait Used',
        max_length=2,
        choices=BAITS,
        default=BAITS[0][0]
    )
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()}"