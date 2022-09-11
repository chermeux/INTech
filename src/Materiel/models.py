from django.db import models
import os
from datetime import datetime

# Cela permet l'enregistrement comptable des factures
class Objet(models.Model):
    id = models.AutoField(primary_key=True)
    CodeBarre = models.TextField(null=True)
    description = models.CharField(max_length=100)
    appartenance = models.TextField(null=True)
    #photoObjet = models.FileField()

    def __str__(self):
        return self.description

class Emprunt(models.Model):
    id = models.AutoField(primary_key=True)
    idObjetEmprunt = models.TextField(null=True)
    NomEmprunteur = models.CharField(max_length=100)
    Caution = models.TextField(null=True)
    DateDebutEmprunt = models.DateField(default=datetime.now(), blank=True)
    DateFinEmprunt = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.NomEmprunteur

class CodeTraitement(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField()
