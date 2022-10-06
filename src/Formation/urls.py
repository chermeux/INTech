from django.contrib import admin
from django.urls import path, include
from .views import indexFormation, Certification, CertificatPersonne, FormationEachPerson, FormationView, QuestionnaireView

urlpatterns = [
    path('indexFormation/', indexFormation,  name='indexFormation_urlpattern_name'),
    path('Certification/', Certification, name='Certification_urlpattern_name'),
    path('CertificatPersonne/', CertificatPersonne, name='CertificatPersonne_urlpattern_name'),
    path('FormationEachPerson/', FormationEachPerson, name='FormationEachPerson_urlpattern_name'),
    path('FormationView/<str:pk>', FormationView, name='FormationView_urlpattern_name'),
    path('QuestionnaireView/<str:pk>', QuestionnaireView, name='QuestionnaireView_urlpattern_name'),
]
