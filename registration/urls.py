from django.urls import path
from django.conf.urls import include,url
from . import views

app_name='registration'

urlpatterns = [
    path("login",views.login,name='login_url'),
    path("register",views.register,name='signup_url'),
    path("otp-verification",views.verify,name='otp_url'),
    path("logout",views.logout,name='logout_url'),
    path("profile",views.view_profile,name='view_profile_url'),
    path("profile/edit",views.edit_profile,name='edit_profile_url'),
    path("change-password",views.change_password,name='change_password_url'),
    path("forgot-password",views.forgot_password,name='forgot_password_url'),
    path("reset-password-otp-verification",views.reset_password_otp_verify,name='reset_password_otp_verify_url'),
    path("reset-password",views.reset_password,name='reset_password_url')
    #url(r'^auth/', include('social_django.urls', namespace='social'))
]
