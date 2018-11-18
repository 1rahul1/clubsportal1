from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'forum/index.html')

def add_post(request):
    return render(request,'forum/add_post.html')

def thread(request):
    return render(request,'forum/thread.html')
