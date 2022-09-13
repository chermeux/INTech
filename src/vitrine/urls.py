from django.contrib import admin
from django.urls import path, include
from .views import Presentation, Partenaires, Evenements

urlpatterns = [
    path('', Presentation,  name='Presentation_urlpattern_name'),
    path('Partenaires/', Partenaires, name='Partenaires_urlpattern_name'),
    path('Evenements/', Evenements, name='Evenements_urlpattern_name'),

]
