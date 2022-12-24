from datetime import date
from django.shortcuts import get_object_or_404, render
from acıktın.models import *

data = {
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
        "genres": restoran.genres.all()
    })
