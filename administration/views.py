from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from propose_join.models import ExistingClub,ProposedClub
from propose_join.forms import club_logo
from django.contrib.auth import get_user_model
from .models import Onpollclub
from datetime import datetime
from django.utils import timezone

from dateutil.relativedelta import relativedelta

User = get_user_model()

def index(request):
    qs = ProposedClub.objects.all()
    return render(request,'administration/ew.html',{"qs":qs})

def result(request):
    ab = ProposedClub.objects.all()
    for a in ab:
        a.delete()
        break;
    fullname1 = request.POST['message']
    send_mail(
        'Your club is rejected',
        fullname1,
        'iiits2021@gmail.com',
        ['saisreeramputta156@gmail.com'],
        fail_silently=False,
    )
    qs = ProposedClub.objects.all()
    return render(request, 'administration/ew.html', {"qs":qs})

# Create your views here.
def result1(request):
    ab = ProposedClub.objects.all()
    for a in ab:
        Onpollclub.objects.create(club_name=a.club_name,admin=a.name,club_info=a.club_info,club_logo=a.club_logo)
        a.delete()
        break;
    send_mail(
        'Your club is accepted',
        'fullname1',
        'iiits2021@gmail.com',
        ['saisreeramputta156@gmail.com'],
        fail_silently=False,
    )
    qs = ProposedClub.objects.all()
    return render(request, 'administration/ew.html', {"qs":qs})



