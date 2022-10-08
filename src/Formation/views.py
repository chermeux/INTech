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
#Cette partie permet d'indiquer les certificats que nous pouvons proposer
@login_required
def AdminFormation(request):
    context = {}
    return render(request, "Formation/AdminFormation.html", context)

#cette partie permet à chaque utilisateur connecté de voir toutes les formations qu'il peut suivre et checker ses certificats
@login_required(login_url='presentation')
def FormationEachPerson(request):
    FormationsDisponibles = Formation.objects.all()
    CertificationsForPerson = Certification.objects.filter(idPersonneCertificat=1)#TODO 1 à remplacer par l'id de la personne quand elle est connectée
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
