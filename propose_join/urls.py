from django.urls import path
from . import views

app_name= "propose_join"
urlpatterns=[
    path('button', views.model_form_upload, name='button'),
    path('list', views.list, name='list'),

]
