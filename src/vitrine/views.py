from django.shortcuts import render

# Create your views here.
def Presentation(request):
    return render(request, "vitrine/Presentation.html")

def Partenaires(request):
    return render(request, "vitrine/Partenaires.html")
