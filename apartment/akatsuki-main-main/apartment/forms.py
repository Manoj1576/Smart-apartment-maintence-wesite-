from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'rent', 'electricity', 'water', 'food', 'parking']

