from django.urls import path
from . import views

app_name= "propose_join"
urlpatterns=[
    path('button', views.model_form_upload, name='button'),
    path('list', views.list, name='list'),
    path('existing',views.existingclub,name='existing'),
    path('existing/add', views.add_to_join, name='add_to_join'),
    path('myclub', views.joined, name='myclub')

]
