from django.contrib import admin
from django.urls import path, include
from .views import Presentation, Partenaires, Evenements,ContactView,ArticlesLegaux

urlpatterns = [
    path('', Presentation,  name='Presentation_urlpattern_name'),
    path('Partenaires/', Partenaires, name='Partenaires_urlpattern_name'),
    path('Evenements/', Evenements, name='Evenements_urlpattern_name'),
    path('contact/',ContactView, name='Contact_urlpattern_name'),
    path('LoisRegles/<str:pk>/',ArticlesLegaux, name='ArticlesLegaux_urlpattern_name'),
]
