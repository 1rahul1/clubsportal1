from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ExistingClub,ProposedClub
from .forms import club_logo
from django.contrib.auth import get_user_model
from registration.models import Profile

User = get_user_model()


from .models import CustomUser

def list(request):
    qs = ProposedClub.objects.all()
    return render(request,"propose_join/list.html",{"qs":qs})

def model_form_upload(request):
    form = club_logo(request.POST, request.FILES)
    if request.method == 'POST':
        form = club_logo(request.POST, request.FILES)
        print(request.user)

        print(request.POST)
        if form.is_valid():
            club1 = form.save(commit=False)
            club1.name =Profile.objects.get(user=request.user)
            #CustomUser.objects.get(Username=request.user)
            club1.save()
            return render(request,'propose_join/next.html')
    else:
        form = club_logo()
    return render(request, 'propose_join/home.html', {
        'form': form
    })
