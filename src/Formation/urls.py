from django.contrib import admin
from django.urls import path, include
from .views import AdminFormation, FormationEachPerson, FormationView,Formationadd,UpdateFormation,CertificationEncoursView, QuestionnaireView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('AdminFormation/', AdminFormation,  name='AdminFormation_urlpattern_name'),
    path('Formationadd/', Formationadd,  name='AddFormation_urlpattern_name'),
    path('FormationEachPerson/', FormationEachPerson, name='FormationEachPerson_urlpattern_name'),
    path('FormationView/<str:pk>', FormationView, name='FormationView_urlpattern_name'),
    path('QuestionnaireView/<str:pk>', QuestionnaireView, name='QuestionnaireView_urlpattern_name'),
    path('UpdateFormation/<str:pk>', UpdateFormation, name='UpdateFormation_urlpattern_name'),
    path('CertificationEncours/',CertificationEncoursView, name='CertificationEncours_urlpattern_name'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
