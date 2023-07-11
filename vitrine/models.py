from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Partenairesbdd(models.Model):
    id = models.AutoField(primary_key=True)
    NomPartenaire = models.TextField(null=True)
    Description = models.TextField(null=True)
    Image = models.ImageField(upload_to='img', null=True, blank=True)
    SiteWeb = models.TextField(null=True)

    def __str__(self):
        return self.NomPartenaire

class Evenementsbdd(models.Model):
    id = models.AutoField(primary_key=True)
    TitreEvenement = models.TextField(null=True)
    Description = models.TextField(null=True)
    Image = models.FileField()

    def __str__(self):
        return self.TitreEvenement

class Parametres(models.Model):
    LogoFooterAssociation = models.ImageField(upload_to='img', null=True, blank=True)
    LogoFooterEcoles = models.ImageField(upload_to='img', null=True, blank=True)
    MentionsLegales = HTMLField()
    PolitiqueDeConfidentialite = HTMLField()
    AdresseMail = models.CharField(max_length=100)
    NumeroTelephone = models.CharField(max_length=500)
    Adresse = models.CharField(max_length=100)
    Ville = models.CharField(max_length=100)
    PhotoCouverture = models.ImageField(upload_to='img', null=True, blank=True)
    NomAssociationBasPage = models.CharField(max_length=120)
    lienDrive = models.TextField(null=True)
    lienGit = models.TextField(null=True)


    def __str__(self):
        return self.NomAssociationBasPage

