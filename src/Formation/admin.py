from django.contrib import admin

from .models import PersoneAvecCertificat, Certificat

admin.site.register(Certificat)
admin.site.register(PersoneAvecCertificat)
