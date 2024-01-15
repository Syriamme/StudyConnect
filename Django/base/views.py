from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    rooms = Room.objects.all()
    room = None

    for i in rooms:
        if i.id == int(pk):
            room = i
            break  # Once the room is found, exit the loop

    context = {'room': room}
    return render(request, 'base/room.html', context)
