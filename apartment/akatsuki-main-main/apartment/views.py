from django.shortcuts import render,redirect
from .forms import RoomForm
from .models import Room

from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room

def room_input(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('display_rooms')  # Redirect to the display page after saving
    else:
        form = RoomForm()
    return render(request, 'blog/ad_bills.html', {'form': form})

def display_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'blog/bills.html', {'rooms': rooms})

# def room_input(request):
#     if request.method == 'POST':
#         # Get data from the form
#         room_number = request.POST.get('room_number')
#         rent = request.POST.get('rent')
#         electricity = request.POST.get('electricity')
#         water = request.POST.get('water')
#         food = request.POST.get('food')
#         parking = request.POST.get('parking')

#         # Save the data to the database
#         Room.objects.create(
#             room_number=room_number,
#             rent=rent,
#             electricity=electricity,
#             water=water,
#             food=food,
#             parking=parking
#         )
#         return redirect('display_rooms')  # Redirect to the display page after saving
#     return render(request, 'blog/ad_bills.html')

# def display_rooms(request):
#     rooms = Room.objects.all()
#     return render(request, 'blog/bills.html', {'rooms': rooms})

# def room_input(request):
#     if request.method == 'POST':
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('display_rooms')  # Redirect to the display page after saving
#     else:
#         form = RoomForm()
#     return render(request, 'blog/ad_bills.html', {'form': form})