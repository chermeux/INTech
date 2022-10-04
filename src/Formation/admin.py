from django.contrib import admin
from .models import PersoneAvecCertificat, Formation, PersoneEnCoursCertification

admin.site.register(Formation)
admin.site.register(PersoneAvecCertificat)
admin.site.register(PersoneEnCoursCertification)
