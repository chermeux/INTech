from django.db import models

class MembreINTech(models.Model):
    id = models.AutoField(primary_key=True)
    Nom = models.TextField(null=True)
    Prenom = models.TextField(null=True)
    Ecole = models.TextField(null=True)
    mail = models.TextField(null=True)
    mdp = models.TextField(null=True)
    role = models.TextField(null=True)
    ValidationCompte = models.TextField(null=True)

    def __str__(self):
        return self.mail
