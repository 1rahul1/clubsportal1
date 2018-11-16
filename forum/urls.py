from django.urls import path

from . import views

urlpatterns = [
    path("",views.index),
    path("addpost",views.add_post),
    path("thread",views.thread),
]
