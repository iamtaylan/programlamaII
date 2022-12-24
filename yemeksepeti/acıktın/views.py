from datetime import date
from django.shortcuts import render

data = {
    "restoranlar": [
        {
            "title": "restoran adı 1",
            "aciklama": "aciklama 1",
            "coverImage": "cover1.jpg",
            "imageUrl": "m1.jpg",
            "begenme": "64%",
            "oySayi": "9,981",
            "acikKapali": "acik",
            "slug": "menu-1",
            "date": date(1973,10,10)
        },
        {
            "title": "restoran adı 2",
            "aciklama": "aciklama 2",
            "imageUrl": "m2.jpg",
            "coverImage": "cover2.jpg",
            "begenme": "75%",
            "oySayi": "4,712",
            "acikKapali": "acik",
            "slug": "menu-2",
            "date": date(2003,5,10)
        },
        {
            "title": "restoran adı 3",
            "aciklama": "aciklama 3",
            "imageUrl": "m3.jpg",
            "coverImage": "cover3.jpg",
            "begenme": "91%",
            "oySayi": "29,426",
            "acikKapali": "acik",
            "slug": "menu-3",
            "date": date(1989,5,5)
            
        },
        {
            "title": "restoran adı 4",
            "aciklama": "aciklama 4",
            "imageUrl": "m4.jpg",
            "coverImage": "cover1.jpg",
            "begenme": "87%",
            "oySayi": "12,492",
            "acikKapali": "acik",
            "slug": "menu-4",
            "date": date(2012,12,4)
        },
    ],
    "sliders":[ 
        {
            "slider_image": "slider1.jpg",
            "slider_url": "menu-1"
        },
        {
            "slider_image": "slider2.jpg",
            "slider_url": "menu-2"
        },
        {
            "slider_image": "slider3.jpg",
            "slider_url": "menu-3"
        },
    ],


}




# Create your views here.

def index(request):
    restoranlar = data["restoranlar"][0:4]
    sliders = data["sliders"]
    return render(request,'index.html', {
        "restoranlar": restoranlar,
        "sliders": sliders
    })

def restoranlar(request):
    restoranlar = data["restoranlar"]
    return render(request,'restoranlar.html',{
        "restoranlar": restoranlar,
    })
        
def menuler(request, slug):
    restoranlar = data["restoranlar"]

    selectedRestoran = None
    for restoran in restoranlar:
        if restoran["slug"] == slug:
            selectedRestoran = restoran

    return render(request,'menuler.html', {
        "restoran":selectedRestoran
    })
