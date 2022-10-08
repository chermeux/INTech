from django.contrib import admin
from django.urls import path
from .views import signin, signout, signup, Outils

urlpatterns = [
    path('signin/', signin,  name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('Outils/', Outils, name='Outils'),

]
