from django.db import models

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from dateutil.relativedelta import relativedelta


# Create your models here.
User = get_user_model()



class CustomUser(models.Model):
    Name     = models.CharField(max_length=200)
    GENDER_CHOICE=(
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    )
    Gender   = models.CharField(max_length=1, choices=GENDER_CHOICE)
    STUDENT=1
    PROFESSOR=2
    ADMINISTRATION=3
    PROFESSION_CHOICE=(
        (STUDENT,'student'),
        (PROFESSOR,'professor'),
        (ADMINISTRATION,'administration')
    )
    Profession=models.PositiveSmallIntegerField(choices=PROFESSION_CHOICE)
    BATCH_CHOICE=(
        ('UG1','UNDER GRADUATE 1'),
        ('UG2','UNDER GRADUATE 2'),
        ('UG3','UNDER GRADUATE 3'),
        ('UG4','UNDER GRADUATE 4'),
        ('PG','POST GRADUATE '),
    )
    Batch=models.CharField(max_length=20,choices=BATCH_CHOICE)
    Dob=models.DateField(max_length=8)
    age=models.IntegerField()

    Username = models.OneToOneField(User,on_delete=models.PROTECT)
    email    = models.EmailField(unique=True)


    def __str__(self):
        today=date.today()
        delta=relativedelta(today,self.Dob)
        return str(delta.years)


    def __str__(self):
        return str(self.Name)




class ProposedClub(models.Model):
    name=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    club_name=models.CharField(max_length=200,unique=True)
    club_info =models.TextField(max_length=20000)
    club_logo=models.ImageField(upload_to='media_/club_logo',)

    def __str__(self):
        return  str(self.club_name) + " by " + str(self.name)



class ExistingClub(models.Model):
    club_name  = models.CharField(max_length=200,unique=True)
    admin = models.ManyToManyField(CustomUser)
    club_info  =models.TextField(max_length=20000)
    club_logo = models.ImageField(upload_to='media_/club_logo', blank=True)

    def __str__(self):
        return str(self.club_name) + " admin--> " + str(self.admin)



class ClubMember(models.Model):
    user_name = models.OneToOneField(CustomUser,on_delete=models.PROTECT)
    clubs_joined = models.ManyToManyField(ExistingClub)

    def __str__(self):
        return str(self.user_name)
