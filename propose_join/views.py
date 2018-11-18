from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ExistingClub,ProposedClub
from .forms import club_logo
from django.contrib.auth import get_user_model
from registration.models import Profile
from django.contrib.auth.models import UserManager
from django.contrib.auth.decorators import login_required

User = get_user_model()
from django.shortcuts import get_object_or_404


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

            club1.save()
            return render(request,'propose_join/next.html')
    else:
        form = club_logo()
    return render(request, 'propose_join/home.html', {
        'form': form
    })

def existingclub(request):
    mem=request.user
    qs = ExistingClub.objects.exclude(members=mem)
    return render(request,"propose_join/existing.html",{"qs":qs})

@login_required
def add_to_join(request):
    if request.method == "POST":
        clubname=request.POST.get('club-joined')
        print(request.user)
        cuser = request.user
        existingclub = ExistingClub.objects.get(club_name=clubname)
        existingclub.members.add(cuser)

        return redirect("propose_join:existing")

    else:

        return redirect("home:index")

def joined(request):
    mem=request.user
    qs=ExistingClub.objects.filter(members=mem)
    print(qs)
    return render(request, "propose_join/myclub.html", {"qs": qs})