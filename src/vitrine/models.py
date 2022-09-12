from django.db import models

# Create your models here.
class Partenairesbdd(models.Model):
    id = models.AutoField(primary_key=True)
    NomPartenaire = models.TextField(null=True)
    Description = models.TextField(null=True)
    Image = models.FileField()
    SiteWeb = models.TextField(null=True)

    def __str__(self):
        return self.NomPartenaire
