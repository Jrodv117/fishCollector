from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Location 
from .forms import BaitForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/index.html', { 'fishes': fishes })

def fishes_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    id_list = fish.locations.all().values_list('id')
    locations_fish_doesnt_have = Location.objects.exclude(id__in=id_list)
    bait_form = BaitForm()
    return render(request, 'fishes/details.html', {'fish': fish, 'bait_form': bait_form, 'locations': locations_fish_doesnt_have})

def add_bait(request, fish_id):
  form = BaitForm(request.POST)
  if form.is_valid():
    new_bait = form.save(commit=False)
    new_bait.fish_id = fish_id
    new_bait.save()
  return redirect('detail', fish_id=fish_id)

def assoc_location(request, fish_id, location_id):
  Fish.objects.get(id=fish_id).locations.add(location_id)
  return redirect('detail', fish_id=fish_id)

class FishCreate(CreateView):
    model = Fish
    fields = ['kind', 'description']

class FishUpdate(UpdateView):
    model = Fish
    fields = '__all__'

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fishes/'
  
class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'
  