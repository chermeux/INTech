import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageEnhance
import datetime
import os


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

# Create your views here.
def EmpruntRecensementMateriel(request):
    photoTake = 0
    CodeBarre =12345
    #img = Image.open('./import/IMG_4459.jpg')
    #imgGray = img.convert('L')
    #imgGray.save('./import/test_gray.jpg')

    # read the image
    #im = Image.open("./import/test_gray.jpg")

    # image brightness enhancer
    #enhancer = ImageEnhance.Contrast(im)
    #factor = 5.5  # increase contrast
    #im_output = enhancer.enhance(factor)
    #im_output.save('./import/test.png')

    message = "Message par défaut"
    ####### sous-partie 1 - enregistrer photo et éléments factures #######
    nomdossier = request.user.id
    if request.method == "POST":
        image = request.POST.get('canvas')
        PhotoCodeBarreTraitement = CodeTraitement.objects.create(image=base64_file(image))
        PhotoCodeBarreTraitement.save()
        ####### sous-partie 2 - enregistrer et renommer la facture au bon endroit #######
        path = os.path.dirname(os.path.dirname(__file__)) + "\import"
        path1 = os.path.join(path, str(PhotoCodeBarreTraitement.image))
        oldName, ext = os.path.splitext(str(PhotoCodeBarreTraitement.image))
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if not ext in valid_extensions:
            os.remove(path1)
        else:
            newName = str(PhotoCodeBarreTraitement.id) + ext
            newPath = os.path.join(path, newName)
            os.rename(path1, newPath)
            PhotoCodeBarreTraitement.image.name = newName
            PhotoCodeBarreTraitement.save()
            PhotoCodeBarreTraitement.image.name = newName
            PhotoCodeBarreTraitement.save()
        NameImage = PhotoCodeBarreTraitement.image
        NameImageId = PhotoCodeBarreTraitement.id
        img = Image.open('./import/%s' % NameImage)
        imgGray = img.convert('L')
        imgGray.save('./import/Convert_gray_%s.jpg' % NameImageId)

        # read the image
        im = Image.open("./import/Convert_gray_%s.jpg" % NameImageId)

        # image brightness enhancer
        enhancer = ImageEnhance.Contrast(im)
        factor = 5.5  # increase contrast
        im_output = enhancer.enhance(factor)
        im_output.save('./import/more-contrast-image_%s.png' % NameImageId)

        # read the image in numpy array using cv2
        img = cv2.imread('./import/more-contrast-image_%s.png' % NameImageId)

        # Decode the barcode image
        detectedBarcodes = decode(img)

        # If not detected then print the message
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
            message = "Problème pour lire le code barre, veuillez re-tester"
        else:
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:
                # Locate the barcode position in image
                (x, y, w, h) = barcode.rect
                # Put the rectangle in image using
                # cv2 to heighlight the barcode
                cv2.rectangle(img, (x - 10, y - 10),
                              (x + w + 10, y + h + 10),
                              (255, 0, 0), 2)
                if barcode.data != "":
                    # Print the barcode data
                    CodeBarre = barcode.data
                    CodeBarre = str(CodeBarre)
                    CodeBarre = CodeBarre[1:-1]
                    CodeBarre = CodeBarre[1::]
            message = "Code Barre correctement traité"
        os.remove('./import/more-contrast-image_%s.png' % NameImageId)
        os.remove('./import/Convert_gray_%s.jpg' % NameImageId)
        os.remove('./import/%s' % NameImage)
        SupprimerTraitement = CodeTraitement.objects.filter(id=NameImageId)
        SupprimerTraitement.delete()
        return redirect('/Materiel/InfoEmpruntRecensement/%s' % CodeBarre)


    context = {'photoTake': photoTake, 'message': message}
    return render(request, "Materiel/CodeBarreMateriel.html", context)

def InfoEmpruntRecensement(request, pk):
    DesignationObjet = "Inconnue Erreur"
    dateaffichage = datetime.date.today().strftime('%Y-%m-%d')
    AfficherInputRorE = 2
    ObjetsBase = Objet.objects.all()
    ValeurCodeBarre = pk
    ListeClubs = ['INTech','BricolINT']
    for ObjetBase in ObjetsBase:
        if str(pk) == str(ObjetBase.CodeBarre):
            #Alors on veut emprunter l'objet
            AfficherInputRorE = 0 #cette variable prend la valeur 0 ou 1 en fonction de savoir si on emprunte ou on recencence un objet et donc l'affichage html est adapté
            DesignationObjet = Objet.objects.get(CodeBarre=pk)
        else:
            AfficherInputRorE = 1
    if request.method == "POST":
        if AfficherInputRorE == 0:
            NomEmprunteur = request.POST.get('NomEmprunteur')
            DateDebutEmprunt = request.POST.get('DateDebutEmprunt')
            DateFinEmprunt = request.POST.get('DateFinEmprunt')
            Caution = request.POST.get('Caution')
            EmpruntSave = Emprunt.objects.create(idObjetEmprunt=ValeurCodeBarre, NomEmprunteur=NomEmprunteur, DateDebutEmprunt=DateDebutEmprunt, DateFinEmprunt=DateFinEmprunt, Caution=Caution)
            EmpruntSave.save()
        else:
            description = request.POST.get('description')
            appartenance = request.POST.get('appartenance')
            #photoObjet = request.POST.get('photoObjet')
            Rencensement = Objet.objects.create(CodeBarre=ValeurCodeBarre, description=description, appartenance=appartenance) #photoObjet=base64_file(photoObjet)
            Rencensement.save()
        return redirect('/Materiel/EmpruntorRecensement/')
    context = {'AfficherInputRorE': AfficherInputRorE, 'ValeurCodeBarre':ValeurCodeBarre, 'ListeClubs':ListeClubs, 'dateaffichage':dateaffichage, 'DesignationObjet':DesignationObjet}
    return render(request, "Materiel/inforEmpruntOrRencensement.html", context)

