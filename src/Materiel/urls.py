from django.contrib import admin
from django.urls import path, include
from .views import EmpruntMateriel, RecensementMateriel

urlpatterns = [
    path('Emprunt/', EmpruntMateriel,  name='EmpruntMateriel_urlpattern_name'),
    path('RecensementMateriel/', RecensementMateriel, name='RecensementMateriel_urlpattern_name'),
]
