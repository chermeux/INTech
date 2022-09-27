from django.db import models

class Certificat(models.Model):
    id = models.AutoField(primary_key=True)
    NomCertificat = models.TextField(null=True)
    Description = models.TextField(null=True)
    Duree = models.TextField(null=True)
    LienQuestionnaire = models.TextField(null=True)
    LienFormationEcrite = models.TextField(null=True)

    def __str__(self):
        return self.NomCertificat


class PersoneAvecCertificat(models.Model):
    id = models.AutoField(primary_key=True)
    NomPersonne = models.TextField(null=True)
    PrenomPersonne = models.TextField(null=True)
    mailPersonne = models.TextField(null=True)
    NomFormationCertificat = models.TextField(null=True)
    DateCertificat = models.TextField(null=True)

    def __str__(self):
        return self.mailPersonne
