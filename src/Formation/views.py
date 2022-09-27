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


@login_required(login_url='presentation')
def indexFormation(request):
    return render(request, "Formation/indexFormation.html")

#Cette partie permet d'indiquer les certificats que nous pouvons proposer
@login_required(login_url='presentation')
def Certification(request):
    return render(request, "Formation/Certifications.html")

#Cette partie permet d'indiquer les certificats que chaque membre a eu
@login_required(login_url='presentation')
def CertificatPersonne(request):
    return render(request, "Formation/PersonneAvecCertificat.html")
