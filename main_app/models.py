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
class Fish(models.Model):
    kind = models.CharField(max_length=50)
    length = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.kind

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fish_id': self.id})

class Bait(models.Model):
    type = models.CharField(
        'Types of Bait Used',
        max_length=2,
        choices=BAITS,
        default=BAITS[0][0]
    )
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()}"