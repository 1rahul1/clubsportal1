from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls import include

app_name='registration'

urlpatterns = [
    path("login",views.login,name='login_url'),
    path("register",views.register,name='signup_url'),
    path("otp-verification",views.verify,name='otp_url'),
    path("logout",views.logout,name='logout_url'),
]
urlpatterns += [
    url(r'^propose_join/', include('propose_join.urls', namespace='propose_join')),

]