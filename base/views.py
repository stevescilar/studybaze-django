from django.shortcuts import render


rooms = [
    {'id':1,'name':'Lets learn Ps!'},
    {'id':2,'name':'Make it Happen'},
    {'id':3,'name':'Attitude'},
]


def home(request):
    return render(request,'home.html',{'rooms':rooms })

def room(request):
    return render (request,'room.html')