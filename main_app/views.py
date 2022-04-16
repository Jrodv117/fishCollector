from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish
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
    bait_form = BaitForm()
    return render(request, 'fishes/details.html', {'fish': fish, 'bait_form': bait_form})

def add_bait(request, fish_id):
  form = BaitForm(request.POST)
  if form.is_valid():
    new_bait = form.save(commit=False)
    new_bait.fish_id = fish_id
    new_bait.save()
  return redirect('detail', fish_id=fish_id)

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishUpdate(UpdateView):
    model = Fish
    fields = '__all__'

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fishes/'
  