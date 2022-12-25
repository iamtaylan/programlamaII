from datetime import date
from django.shortcuts import get_object_or_404, render
from acıktın.models import *

data = {
    "sliders":[ 
        {
            "slider_image": "sushicoS.jpg",
            "slider_url": "sushico"
        },
        {
            "slider_image": "DominosS.webp",
            "slider_url": "dominos"
        },
        {
            "slider_image": "BurgerKingS.webp",
            "slider_url": "burger"
            
        },
    ],
}

# Create your views here.

def index(request):
    restoranlar = Restoran.objects.filter(is_active = True, is_home = True)
    sliders = data["sliders"]
    return render(request,'index.html', {
        "restoranlar": restoranlar,
        "sliders": sliders
    })

def restoranlar(request):
    restoranlar = Restoran.objects.filter(is_active = True)
    return render(request,'restoranlar.html',{
        "restoranlar": restoranlar,
    })

def menuler(request, slug):

    restoran = get_object_or_404(Restoran, slug=slug)

    return render(request,'menuler.html', {
        "restoran":restoran,
        "genres": restoran.genres.all(),
        "person": restoran.people.all(),
        "videos": restoran.video_set.all()
    })
