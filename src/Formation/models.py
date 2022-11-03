from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from tinymce.models import HTMLField


class Formation(models.Model):
    id = models.AutoField(primary_key=True)
    NomCertificat = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Duree = models.CharField(max_length=100)
    TextFormation = HTMLField()
    Questionnaire = HTMLField()

    def __str__(self):
        return self.NomCertificat


class Certification(models.Model):
    EtatCertificationChoix = (('DemandeValidation', 'DemandeValidation'), ('Validee', 'Validee'), ('',''))
    id = models.AutoField(primary_key=True)
    idPersonneCertificat = models.IntegerField(blank=True, default=0) #TODO Faudrait faire un foreignkey avec le models user mais bug actuellement donc flemme de trouver la solution
    idFormation = models.IntegerField(blank=True, default=0) #TODO Faudrait faire un foreignkey avec le models Formation mais bug actuellement donc flemme de trouver la solution
    EtatCertification = models.TextField(null=True, choices=EtatCertificationChoix)
    DateCertificat = models.DateField(default=datetime.now(),blank=True)

    def __str__(self):
        return self.EtatCertification
