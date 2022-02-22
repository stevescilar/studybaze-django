from django.shortcuts import render


rooms = [
    {'id':1,'name':'Lets learn Ps!'},
    {'id':2,'name':'Make it Happen'},
    {'id':3,'name':'Attitude'},
]


def home(request):
    # create a context dictationary
    context = {'rooms':rooms}
    return render(request,'base/home.html',context) 

def room(request,pk):
    room = None
    for i in rooms:
        if i['id']== int(pk):
            room = i
    context = {'room': room}
    return render (request,'base/room.html',context) 