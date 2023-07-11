import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from User.models import infoMembreINTech
from vitrine.views import getBase

#Cette partie permet d'accéder à l'ajout de formations, les modifications et encore de valider l'obtention d'une formation pour ceux qui font la demande
@login_required
def AdminFormation(request):
    infomembre = infoMembreINTech.objects.get(idCompte=request.user.id)
    context ={}
    if infomembre.role == "Bureau":
        AllFormations = Formation.objects.all()
        lien = 'https://docs.google.com/document/d/e/2PACX-1vT9n15jg5UqUTXggMtCgi0aHMLOwyOlRlWMbGj1ZIH2b8iV7jeC3dZrqQlYxRVAsVCshiNkMv-uPuJZ/pub'
        context ={'AllFormations':AllFormations,'lien':lien}
    else:
        return redirect('/')
    return render(request, "Formation/AdminFormation.html",getBase(request)|context)

#Cela permet à un membre du bureau de créer une formation
@login_required
def Formationadd(request):
    infomembre = infoMembreINTech.objects.get(idCompte=request.user.id)
    if infomembre.role == "Bureau":
        if request.method == "POST":
            NomCertificat = request.POST.get('NomFormation')
            Description = request.POST.get('Description')
            Duree = request.POST.get('Duree')
            Questionnaire = request.POST.get('Questionnaire')
            TextFormation = request.POST.get('FormationDocument')
            FormationAdd = Formation.objects.create(NomCertificat=NomCertificat, Description=Description, Duree=Duree, Questionnaire=Questionnaire, TextFormation=TextFormation)
            FormationAdd.save()
            return redirect('../../Formation/Formationadd/')
    else:
        return redirect('/')
    return render(request, "Formation/FormationAdd.html",getBase(request))

#Cela permet à un membre du bureau de mettre à jour une formation disponible
@login_required(login_url='presentation')
def UpdateFormation(request, pk):
    ViewFormation = Formation.objects.get(id=pk)
    infomembre = infoMembreINTech.objects.get(idCompte=request.user.id)
    if infomembre.role == "Bureau":
        if request.method == "POST":
            NomCertificat = request.POST.get('NomFormation')
            Description = request.POST.get('Description')
            Duree = request.POST.get('Duree')
            Questionnaire = request.POST.get('Questionnaire')
            TextFormation = request.POST.get('FormationDocument')
            UpdateFormation = Formation.objects.filter(id=pk).update(NomCertificat=NomCertificat, Description=Description, Duree=Duree, Questionnaire=Questionnaire, TextFormation=TextFormation)
            CertificationDeletePasAJour = Certification.objects.filter(idFormation=pk,EtatCertification='DemandeValidation')
            CertificationDeletePasAJour.delete()
            return redirect('../../Formation/FormationEachPerson/')
    else:
        return redirect('/')
    context = {'ViewFormation': ViewFormation}
    return render(request, "Formation/FormationUpdate.html", getBase(request)|context)


#cette partie permet à chaque utilisateur connecté de voir toutes les formations qu'il peut suivre et checker ses certificats
@login_required
def FormationEachPerson(request):
    infomembre = infoMembreINTech.objects.get(idCompte=request.user.id)
    CertificationsForPerson = Certification.objects.filter(idPersonneCertificat=request.user.id)
    listID =[]
    listIDFValide = []
    listIDFEnCoursValide = []
    for IDCertificationsForPerson in CertificationsForPerson:
        if IDCertificationsForPerson.EtatCertification == "Validee":
            listIDFValide.append(IDCertificationsForPerson.idFormation)
        else :
            listIDFEnCoursValide.append(IDCertificationsForPerson.idFormation)
        listID.append(IDCertificationsForPerson.idFormation)
    FormationsValidee = Formation.objects.filter(id__in=listIDFValide)
    FormationsEnCoursValide = Formation.objects.filter(id__in=listIDFEnCoursValide)
    FormationsDisponibles = Formation.objects.exclude(id__in=listID)
    #TODO Modifier c'est du bricolage, il faut modifier la bdd pour que ce soit des foreign key puis il sera possible de faire une jointure django comme ça existe une option bien faite, donc ça permettra aussi de réduire le template associé là c'est du bricolage rapide mais moche et à modifier de manière urgente !
    context = {'FormationsDisponibles':FormationsDisponibles, 'FormationsValidee':FormationsValidee, 'FormationsEnCoursValide':FormationsEnCoursValide, 'infomembre':infomembre}
    return render(request, "Formation/FormationEachPerson.html", getBase(request)|context)

#Cela permet d'afficher le contenu de chaque formation
@login_required(login_url='presentation')
def FormationView(request, pk):
    ViewFormation = Formation.objects.get(id=pk)
    context = {'ViewFormation':ViewFormation}
    return render(request, "Formation/FormationView.html", getBase(request)|context)

#Cela permet d'afficher le contenu de chaque formation
@login_required(login_url='presentation')
def QuestionnaireView(request, pk):
    ViewFormation = Formation.objects.get(id=pk)
    if request.method == "POST":
        CertificationDemande = Certification.objects.create(idPersonneCertificat=request.user.id, idFormation=pk, EtatCertification='DemandeValidation')
        CertificationDemande.save()
        return redirect('../../Formation/FormationEachPerson/')
    context = {'ViewFormation':ViewFormation}
    return render(request, "Formation/QuestionnaireView.html", getBase(request)|context)

#Cela permet d'afficher ceux qui ont fait une demande de certification pour ensuite pour valider ou non celles-ci
@login_required(login_url='presentation')
def CertificationEncoursView(request):
    infomembre = infoMembreINTech.objects.get(idCompte=request.user.id)
    ViewFormations = Formation.objects.all()
    UserAll = User.objects.all()
    CertificationDemande = Certification.objects.filter(EtatCertification='DemandeValidation')
    if infomembre.role == "Bureau":
        if request.method == "POST":
            id = request.POST.get('id')
            CertificationValidation = Certification.objects.filter(id=id).update(EtatCertification='Validee')
            return redirect('../../Formation/CertificationEncours/')
    else:
        return redirect('/')
# TODO Modifier c'est du bricolage, il faut modifier la bdd pour que ce soit des foreign key puis il sera possible de faire une jointure django comme ça existe une option bien faite, donc ça permettra aussi de réduire le template associé là c'est du bricolage rapide mais moche et à modifier de manière urgente !
    context = {'CertificationDemande':CertificationDemande,'ViewFormations':ViewFormations,'UserAll':UserAll}
    return render(request, "Formation/ValidationCertification.html", getBase(request)|context)
