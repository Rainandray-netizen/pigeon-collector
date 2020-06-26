from django.shortcuts import render

class Pigeon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

pigeons = [
  Pigeon('Roy Pigeon', 'A hardworking salarypigeon trying to make ends meet. Husband to Sandra Pigeon', 3),
  Pigeon('Sandra Pigeon', 'A proud mother, wife of Roy Pigeon', 4),
  Pigeon('Egg', 'An egg', 0)
]

def about(request):
  return render(request, 'about.html')

def home(request):
  return render(request, 'home.html')

def pigeons_index(request):
  return render(request, 'pigeons/index.html', { 'pigeons': pigeons })