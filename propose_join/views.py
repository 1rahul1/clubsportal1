from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def propose(request):
    return render(request,'propose_join/propose.html')

def join(request):
    return render(request,'propose_join/join.html')

def poll(request):
    return render(request,'propose_join/poll.html')
