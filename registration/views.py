from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Signup_form , Add_profile,Editprofile_form,LoginForm,Edituser_form
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import login as signin,authenticate,logout as exit
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import random

def send(email):
    global otp
    otp=random.randint(100000,999999)
    mail = EmailMessage('E-mail verification', str(otp) , to=[email])#,fail_silently=True)
    mail.send()
    print(otp)

def register(request):
    if request.method == 'POST':
        form=Signup_form(request.POST)
        form1=Add_profile(request.POST)
        if form.is_valid() and form1.is_valid():
            email=form.data['email']
            send(email)
            firstname=form.data['first_name']
            lastname=form.data['last_name']
            username=form.data['username']
            password1=form.data['password1']
            password2=form.data['password2']
            gender=form.data['gender']
            ug=form.data['ug']
            profession=form.data['profession']
            context={
                'firstname':firstname,
                'lastname':lastname,
                'username':username,
                'email':email,
                'password1':password1,
                'password2':password2,
                'gender':gender,
                'ug':ug,
                'profession':profession
            }
            return render(request,'registration/email-confirmation.html',context)
    else:
        form=Signup_form()
        form1=Add_profile()
    return render(request,'registration/register.html',{'form_inst':form,'form1':form1})

def login(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    signin(request,user)
                    return redirect('/registration/profile')
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is not available')
    else:
        form=LoginForm()
    return render(request,'registration/login.html',{'form_inst':form})

def logout(request):
        exit(request)
        return redirect('/registration/login')

def verify(request):
    if request.method=='POST':
        otp1=request.POST.get('typed_otp')
        if otp1 == str(otp):
            username=request.POST.get('username')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            ug=request.POST.get('ug')
            profession=request.POST.get('profession')
            new_user=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname)
            new_user.set_password(request.POST['password1'])
            new_user.save()
            new_profile=Profile.objects.create(user=new_user,gender=gender,ug=ug,profession=profession)
            new_profile.save()
            return redirect('/registration/login')
        else:
            return HttpResponse('Wrong otp')
    else:
        return HttpResponse('wrong way')

@login_required(login_url="{% url 'registration:login_url' %}")
def view_profile(request):
    user_profile={'user':request.user}
    return render (request,'registration/profile.html',user_profile)

def edit_profile(request):
    if request.method == 'POST':
        form1=Edituser_form(request.POST,instance=request.user)
        form2=Editprofile_form(request.POST,instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/registration/profile')
    else:
        form1=Edituser_form(instance=request.user)
        form2=Editprofile_form(instance=request.user.profile)
    return render(request,'registration/edit_profile.html',{'form1':form1,'form2':form2})

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/registration/profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render (request,'registration/change_password.html',{'form_inst':form})

def forgot_password(request):
    if request.method == 'POST':
        username=request.POST.get('user_name')
        user_email=request.POST.get('user_email')
        send(user_email)
        return render(request,'registration/otp-verification.html',{'username':username})
    else:
        return render(request,'registration/forgot-password.html')

def reset_password_otp_verify(request):
    if request.method == 'POST':
        username=request.POST.get('user_name')
        otp1=request.POST.get('typed_otp')
        if otp1 == str(otp):
            return render(request,'registration/type-new-password.html',{'username':username})
        else:
            return HttpResponse('Wrong otp')
    else:
        return HttpResponse('Wrong Way')

def reset_password(request):
    if request.method == 'POST':
        username=request.POST.get('user_name')
        user=User.objects.get(username=username)
        user.set_password(request.POST['new_password'])
        user.save()
        return redirect('/registration/login')
    else:
        return HttpResponse('Wrong way')
