from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
  path('pigeons/', views.pigeons_index, name='index'),
	path('pigeons/<int:pigeon_id>/', views.pigeons_detail, name='detail'),
	path('pigeons/create', views.PigeonCreate.as_view(), name='pigeons_create'),
	path('pigeons/<int:pk>/update/', views.PigeonUpdate.as_view(), name='pigeons_update'),
  path('pigeons/<int:pk>/delete/', views.PigeonDelete.as_view(), name='pigeons_delete'),
	path('pigeons/<int:pigeon_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
	path('pigeons/<int:pigeon_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]