import base64

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
import cv2
from pyzbar.pyzbar import decode

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

# Create your views here.
def EmpruntMateriel(request):
    photoTake = 0
    img = cv2.imread('./import/code_barre.png')
    for code in decode(img):
        print(code.type)
        print(code.data.decode('utf-8'))

    ####### sous-partie 1 - enregistrer photo et éléments factures #######
    nomdossier = request.user.id
    if request.method == "POST":
        image = request.POST.get('canvas')
        PhotoCodeBarreTraitement = CodeTraitement.objects.create(image=base64_file(image))
        PhotoCodeBarreTraitement.save()

        img = cv2.imread('./import/QRcode.png')
        det = cv2.QRCodeDetector()
        info, box_coordinates, _ = det.detectAndDecode(img)

        if box_coordinates is None:
            print('No Code')
        else:
            print(info)

        if box_coordinates is not None:
            box_coordinates = [box_coordinates[0].astype(int)]
            n = len(box_coordinates[0])
            for i in range(n):
                cv2.line(img, tuple(box_coordinates[0][i]), tuple(box_coordinates[0][(i + 1) % n]), (0, 255, 0), 3)

        return redirect('/Materiel/Emprunt/')
    context = {'photoTake': photoTake}
    return render(request, "Materiel/EmpruntMateriel.html", context)

def RecensementMateriel(request):
    return render(request, "Materiel/RecensementMateriel.html")
