from django.urls import path

from . import views

urlpatterns = [
    path("propose",views.propose)
]
