from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    #id=models.AutoField(primary_key=True)
    gender_choices = (
        ('Male','Male'),
        ('Female','Female'),
        ('others','Others'),
    )
    ug_choices = (
        ('UG1','UG1'),
        ('UG2','UG2'),
        ('UG3','UG3'),
        ('UG4','UG4'),
    )
    profession_choices = (
        ('UG','UG'),
        ('PHD','PHD'),
        ('TS','Teaching Staff'),
        ('NTS','Non Teaching Staff')
    )
    gender = models.CharField(max_length=6,choices=gender_choices,default='')
    ug = models.CharField(max_length=3,choices=ug_choices,default='')
    profession = models.CharField(max_length=3,choices=profession_choices,default='')

    def __str__(self):
        return self.user.username
