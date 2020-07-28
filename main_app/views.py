from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pigeon as PigeonModel
from .models import Toy as ToyModel
from .forms import FeedingForm

class Pigeon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

class PigeonCreate(CreateView):
  model = PigeonModel
  fields = ['name', 'description', 'age']

class PigeonUpdate(UpdateView):
  model = PigeonModel
  fields = ['breed', 'description', 'age']

class PigeonDelete(DeleteView):
  model = PigeonModel
  success_url = '/pigeons/'

def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

def pigeons_index(request):
  pigeons = PigeonModel.objects.all()
  return render(request, 'pigeons/index.html', { 'pigeons': pigeons })

def pigeons_detail(request, pigeon_id):
  pigeon = PigeonModel.objects.get(id=pigeon_id)
  feeding_form = FeedingForm()
  toys_pigeon_doesnt_have = ToyModel.objects.exclude(id__in = pigeon.toys.all().values_list('id'))
  return render(request, 'pigeons/detail.html', { 
    'pigeon': pigeon,
    'feeding_form':feeding_form,
    'toys':toys_pigeon_doesnt_have
  })

def add_feeding(request, pigeon_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.pigeon_id = pigeon_id
    new_feeding.save()
  return redirect('detail', pigeon_id=pigeon_id)

def assoc_toy(request, pigeon_id, toy_id):
  PigeonModel.objects.get(id=pigeon_id).toys.add(toy_id)
  return redirect('detail', pigeon_id=pigeon_id)

def unassoc_toy(request, pigeon_id, toy_id):
  PigeonModel.objects.get(id=pigeon_id).toys.remove(toy_id)
  return redirect('detail', pigeon_id=pigeon_id)

class ToyList(ListView):
  model = ToyModel

class ToyDetail(DetailView):
  model = ToyModel

class ToyCreate(CreateView):
  model = ToyModel
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = ToyModel
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = ToyModel
  success_url = '/toys/'