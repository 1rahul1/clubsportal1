from django.urls import path
from . import views

urlpatterns=[
    path('button', views.model_form_upload, name='button'),
    path('list', views.list, name='list'),

]