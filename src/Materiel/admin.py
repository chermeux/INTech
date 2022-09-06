from django.contrib import admin

from .models import Emprunt, Objet, CodeTraitement

admin.site.register(Emprunt)
admin.site.register(Objet)
admin.site.register(CodeTraitement)
# Register your models here.
