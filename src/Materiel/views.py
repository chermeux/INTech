import base64

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import *
import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageEnhance

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

# Create your views here.
def EmpruntMateriel(request):
    photoTake = 0
    img = Image.open('./import/IMG_4459.jpg')
    imgGray = img.convert('L')
    imgGray.save('./import/test_gray.jpg')

    # read the image
    im = Image.open("./import/test_gray.jpg")

    # image brightness enhancer
    enhancer = ImageEnhance.Contrast(im)
    factor = 5.5  # increase contrast
    im_output = enhancer.enhance(factor)
    im_output.save('./import/test.png')

    message = "Message par défaut"
    ####### sous-partie 1 - enregistrer photo et éléments factures #######
    nomdossier = request.user.id
    if request.method == "POST":
        image = request.POST.get('canvas')
        PhotoCodeBarreTraitement = CodeTraitement.objects.create(image=base64_file(image))
        PhotoCodeBarreTraitement.save()

        img = Image.open('./import/image.png')
        imgGray = img.convert('L')
        imgGray.save('./import/test_gray.jpg')

        # read the image
        im = Image.open("./import/test_gray.jpg")

        # image brightness enhancer
        enhancer = ImageEnhance.Contrast(im)
        factor = 5.5  # increase contrast
        im_output = enhancer.enhance(factor)
        im_output.save('./import/more-contrast-image.png')

        # read the image in numpy array using cv2
        img = cv2.imread('./import/more-contrast-image.png')

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
                    print(barcode.data)
                    CodeBarre = barcode.data
                    print(barcode.type)
            message = "Code Barre correctement traité"

        return redirect('/Materiel/Emprunt/')
    context = {'photoTake': photoTake, 'message': message}
    return render(request, "Materiel/EmpruntMateriel.html", context)

def RecensementMateriel(request):
    return render(request, "Materiel/RecensementMateriel.html")
