from django.contrib import admin
from django.urls import path, include
from .views import indexFormation, Certification, CertificatPersonne

urlpatterns = [
    path('indexFormation/', indexFormation,  name='indexFormation_urlpattern_name'),
    path('Certification/', Certification, name='Certification_urlpattern_name'),
    path('CertificatPersonne/', CertificatPersonne, name='CertificatPersonne_urlpattern_name'),
]
