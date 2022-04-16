from django.forms import ModelForm
from .models import Bait

class BaitForm(ModelForm):
    class Meta:
        model = Bait
        fields = ['type']