from datetime import date
from django.shortcuts import render

data = {
    "restoranlar": [
        {
            "title": "restoran adı 1",
            "aciklama": "aciklama 1",
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
            "begenme": "87%",
            "oySayi": "12,492",
            "acikKapali": "acik",
            "slug": "menu-4",
            "date": date(2012,12,4)
        }
    ],
    "slider": [],


}




# Create your views here.

def index(request):
    restoranlar = data["restoranlar"]
    return render(request,'index.html', {
        "restoranlar": restoranlar,
    })

def restoranlar(request):
    return render(request,'restoranlar.html')

def menuler(request, slug):
    return render(request,'menuler.html', {
        slug:slug
    })
