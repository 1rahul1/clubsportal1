# Generated by Django 2.1.2 on 2018-11-18 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propose_join', '0002_auto_20181118_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Username',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]