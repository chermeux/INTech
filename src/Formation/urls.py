from django.contrib import admin
from django.urls import path, include
from .views import AdminFormation, FormationEachPerson, FormationView, QuestionnaireView

urlpatterns = [
    path('AdminFormation/', AdminFormation,  name='AdminFormation_urlpattern_name'),
    path('FormationEachPerson/', FormationEachPerson, name='FormationEachPerson_urlpattern_name'),
    path('FormationView/<str:pk>', FormationView, name='FormationView_urlpattern_name'),
    path('QuestionnaireView/<str:pk>', QuestionnaireView, name='QuestionnaireView_urlpattern_name'),
]
