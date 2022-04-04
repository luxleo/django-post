from django.shortcuts import render,redirect
from django.http import HttpResponse as hr
from .models import Room
from .forms import RoomForm
#rooms = [{'id':1, 'name':'Let\'s learn python'},
#{'id':2, 'name':'Design with me'},
#{'id':3,'name':'Front end!'}]
def home(req):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(req,'api/home.html',context)
def room(req,pk):
    room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(req,'api/room.html',context)
def createRoom(req):
    form = RoomForm()
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            #'home' is name of '' url
            return redirect('home')
    context = {'form':form}
    return render(req, 'api/room_form.html',context)
def updateRoom(req,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    if req.method == 'POST':
        form = RoomForm(req.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(req,'api/room_form.html',context)
def deleteRoom(req,pk):
    room = Room.objects.get(id = pk)
    if req.method== 'POST':
        room.delete()
        return redirect('home')
    return render(req,'api/delete.html',{'obj':room})
# Create your views here.
