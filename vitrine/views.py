from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import Partenairesbdd, Evenementsbdd,Parametres

# Create your views here.
def getBase(request):
    return {'ParametresGlobaux': Parametres.objects.latest('id')}

def Presentation(request):
    return render(request, "vitrine/Presentation.html", getBase(request))

def Evenements(request):
    EvenementsViews = Evenementsbdd.objects.all()
    context = {'EvenementsViews': EvenementsViews}
    return render(request, "vitrine/Evenements.html", getBase(request)|context)

def Partenaires(request):
    PartenairesViews = Partenairesbdd.objects.all()
    context = {'PartenairesViews':PartenairesViews}
    return render(request, "vitrine/Partenaires.html", getBase(request)|context)

def ContactView(request):
    return render(request, "vitrine/Contact.html",getBase(request))

def ArticlesLegaux(request,pk):
    ParametreAlire = Parametres.objects.latest('id')
    context = {'ArticleAMettre': ParametreAlire.MentionsLegales}
    if pk == '1':
        context = {'ArticleAMettre':ParametreAlire.MentionsLegales}
    else:
        context = {'ArticleAMettre': ParametreAlire.PolitiqueDeConfidentialite}
    return render(request, "vitrine/ArticlesReglesLois.html",getBase(request)|context)
