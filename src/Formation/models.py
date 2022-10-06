from django.db import models

class Formation(models.Model):
    id = models.AutoField(primary_key=True)
    NomCertificat = models.TextField(null=True)
    Description = models.TextField(null=True)
    Duree = models.TextField(null=True)
    LienQuestionnaire = models.TextField(null=True)
    LienFormationEcrite = models.TextField(null=True)

    def __str__(self):
        return self.NomCertificat

class PersoneEnCoursCertification(models.Model):
    id = models.AutoField(primary_key=True)
    idPersonneCertificat = models.TextField(null=True)
    idFormation = models.TextField(null=True)

    def __str__(self):
        return self.id

class PersoneAvecCertificat(models.Model):
    id = models.AutoField(primary_key=True)
    idPersonneCertificat = models.TextField(null=True)
    idFormation = models.TextField(null=True)
    DateCertificat = models.TextField(null=True)

    def __str__(self):
        return self.id
