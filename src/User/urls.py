from django.contrib import admin
from django.urls import path
from .views import signin, signout, signup

urlpatterns = [
    path('signin/', signin,  name='login_urlpattern_name'),
    path('signout/', signout, name='logout_urlpattern_name'),
    path('signup/', signup, name='signup_urlpattern_name'),
]
