from django.urls import path
from . import views

urlpatterns = [
    path('admin_maintenance/', views.room_input, name='room_input'),
    path('display/', views.display_rooms, name='display_rooms'),
]