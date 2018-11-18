from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class Signup_form(UserCreationForm):
    #password=forms.CharField(widget=forms.PasswordInput())
    first_name=forms.CharField(max_length=50,required=True,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'Firstname*'}))
    last_name=forms.CharField(max_length=50,required=True,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'Lastname*'}))
    username=forms.CharField(max_length=50,required=True,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'Username*'}))
    email=forms.EmailField(max_length=50,required=True,help_text='Required',widget=forms.TextInput(attrs={'placeholder':'Email*'}))
    password1=forms.CharField(label='Password',max_length=50,required=True,help_text='Required',widget=forms.PasswordInput(attrs={'placeholder':'Password*'}))
    password2=forms.CharField(label='Confirm Password',max_length=50,required=True,help_text='Required',widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Password*'}))

    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2']

class Add_profile(forms.ModelForm):
    #dob = forms.DateField(widget=SelectDateWidget)
    class Meta:
        model = Profile
        fields=['gender','profession','ug']

class Edituser_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    class Meta:
        model=User
        fields=(
            'first_name',
            'last_name',
            'username'
        )

class Editprofile_form(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username*'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password*'}))
