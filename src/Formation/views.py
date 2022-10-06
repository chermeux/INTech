import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageEnhance
import datetime
import os
from django.contrib.auth.decorators import login_required

#TODO Mettre une connexion unique administrateur ou bureau
@login_required(login_url='presentation')
def indexFormation(request):
    return render(request, "Formation/indexFormation.html")

#TODO Mettre une connexion unique administrateur ou bureau
#Cette partie permet d'indiquer les certificats que nous pouvons proposer
@login_required(login_url='presentation')
def Certification(request):
    Certificats = Formation.objects.all()
    context = {'Certificats':Certificats}
    return render(request, "Formation/Certifications.html", context)

#TODO Mettre une connexion unique administrateur ou bureau
#Cette partie permet d'indiquer les certificats que chaque membre a eu et de valider ceux en cours de validation
@login_required(login_url='presentation')
def CertificatPersonne(request):
    return render(request, "Formation/PersonneAvecCertificat.html")

#cette partie permet à chaque utilisateur connecté de voir toutes les formations qu'il peut suivre et checker ses certificats
@login_required(login_url='presentation')
def FormationEachPerson(request):

    context = {}
    return render(request, "Formation/FormationEachPerson.html", context)


#Cela permet d'afficher le contenu de chaque formation
@login_required(login_url='presentation')
def FormationView(request, pk):
    context = {}
    return render(request, "Formation/FormationView.html", context)

#Cela permet d'afficher le questionnaire de chaque formation
@login_required(login_url='presentation')
def QuestionnaireView(request, pk):
    if request.method == "POST":
        return redirect('/Formation/FormationEachPerson/')
    context = {}
    return render(request, "Formation/QuestionnaireView.html", context)
