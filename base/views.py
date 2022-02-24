from multiprocessing import context
from this import d
from django.shortcuts import render,redirect
from .models import  Room
from .forms import RoomForm
 

# rooms = [
#     {'id':1,'name':'Lets learn Ps!'},
#     {'id':2,'name':'Make it Happen'},
#     {'id':3,'name':'Attitude'},
# ]


def home(request):
    # querry set
    rooms = Room.objects.all()
    # create a context dictionary
    context = {'rooms':rooms}
    return render(request,'base/home.html',context) 

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render (request,'base/room.html',context) 

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form':form }
    return render(request,'base/room_form.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request,'base/room_form.html',context)

def deleteRoom(request):
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})