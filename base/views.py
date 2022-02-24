from django.shortcuts import render
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
        print(request.POST)
        
    context = { 'form':form }
    return render(request,'base/room_form.html', context)