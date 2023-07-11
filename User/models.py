from django.db import models

class infoMembreINTech(models.Model):
    Roles = (('Membre', 'Membre'), ('Bureau', 'Bureau'))
    id = models.AutoField(primary_key=True)
    idCompte = models.IntegerField()
    Ecole = models.TextField(null=True)
    role = models.CharField(null=True, max_length=100, choices=Roles)
    ValidationCompte = models.BooleanField(default=False)

    def __str__(self):
        return self.role
