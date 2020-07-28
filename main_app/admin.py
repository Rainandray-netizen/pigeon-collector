from django.contrib import admin
from .models import Pigeon, Feeding, Toy

# Register your models here.
admin.site.register(Pigeon)
admin.site.register(Feeding)
admin.site.register(Toy)