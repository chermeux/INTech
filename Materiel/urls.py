from django.contrib import admin
from django.urls import path, include
from .views import EmpruntRecensementMateriel, InfoEmpruntRecensement

urlpatterns = [
    path('EmpruntorRecensement/', EmpruntRecensementMateriel,  name='EmpruntMateriel_urlpattern_name'),
    path('InfoEmpruntRecensement/<str:pk>', InfoEmpruntRecensement, name='InfoEmpruntRecensement_urlpattern_name'),
]
