from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("restoranlar", views.restoranlar),
    path("restoranlar/<slug:slug>", views.menuler)

]

#restoranlar/menu-adi