from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import infoMembreINTech
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

def getBase(request):
    return {'infoMembreINTech': infoMembreINTech.objects.all()}

def signin(request):
    if request.method == "POST":
        mail = request.POST.get('mail')
        mdp = request.POST.get('mdp')
        membre = User.objects.filter(email=mail)
        for mb in membre: #TODO c'est du bricolage mais je sais pas pk je ne peux pas mettre un get
            membre = mb
        infomembre = infoMembreINTech.objects.get(idCompte=membre.id)
        user = authenticate(username=membre.username, password=mdp)
        if user is not None:
            if infomembre.ValidationCompte == True:
                login(request, user)
            else:
                messages.info(request, "Votre compte n'a pas encore été validé par un membre administrateur")
        else:
            messages.info(request, 'Mail ou mot de passe incorrect')
            return redirect('../../User/signin/')
        return redirect('../../User/Outils/')
    return render(request, "User/signin.html")

@login_required(login_url='presentation')
def signout(request):
    logout(request)
    return redirect(reverse(signin))

def signup(request):
    if request.method == "POST":
        Pseudo = request.POST.get('Pseudo')
        Nom = request.POST.get('Nom')
        Prenom = request.POST.get('Prenom')
        Ecole = request.POST.get('Ecole')
        mail = request.POST.get('mail')
        mdp1 = request.POST.get('mdp1')
        mdp2 = request.POST.get('mdp2')
        role = "Membre"
        if mdp1 == mdp2:
            if User.objects.filter(email=mail).exists():
                messages.info(request, "Vous ne pouvez pas utiliser cet email")
                return render(request, 'User/signup.html')
            else:
                UserMembre = User.objects.create_user(username=Pseudo, first_name=Prenom, last_name=Nom, password=mdp1, email=mail)
                UserMembre.save()
                messages.info(request, "Votre compte a été créé avec succès")
                UserMembre = User.objects.get(email=mail)
                CreationInfoCompteMembre = infoMembreINTech.objects.create(idCompte=UserMembre.id, Ecole=Ecole, role=role)
                CreationInfoCompteMembre.save()
                return render(request, 'vitrine/Presentation.html')
        else:
            messages.info(request, "les mots de passe sont différents")

        return redirect('vitrine/Presentation')
    return render(request, "User/signup.html")

@login_required
def Outils(request):
    return render(request, "User/Outils.html")
