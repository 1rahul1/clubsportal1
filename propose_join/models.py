

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from registration.models import Profile


User = get_user_model()


class ProposedClub(models.Model):
    name=models.ForeignKey(Profile,on_delete=models.PROTECT)
    club_name=models.CharField(max_length=200,unique=True)
    club_info =models.TextField(max_length=20000)
    club_logo=models.ImageField(upload_to='media_/club_logo',)

    def __str__(self):
        return  str(self.club_name) + " by " + str(self.name)


class ExistingClub(models.Model):
    club_name  = models.CharField(max_length=200,unique=True)
    admin = models.ManyToManyField(User,related_name="club_admin")
    club_info  =models.TextField(max_length=20000)
    club_logo = models.ImageField(upload_to='media_/club_logo', blank=True)
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.club_name)
