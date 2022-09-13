from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Partenairesbdd, Evenementsbdd

# Create your views here.
def Presentation(request):
    return render(request, "vitrine/Presentation.html")

def Evenements(request):
    EvenementsViews = Evenementsbdd.objects.all()
    context = {'EvenementsViews': EvenementsViews}
    return render(request, "vitrine/Evenements.html", context)

def Partenaires(request):
    PartenairesViews = Partenairesbdd.objects.all()
    context = {'PartenairesViews':PartenairesViews}
    return render(request, "vitrine/Partenaires.html", context)

