from django.shortcuts import render
from .models import  Room
 

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