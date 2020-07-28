from django.db import models
from django.urls import reverse

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

MEALS = (
  ('B','Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Pigeon(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'pigeon_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length = 1,
    choices = MEALS,
    default=MEALS[0][0]
  )

  pigeon = models.ForeignKey(Pigeon, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']