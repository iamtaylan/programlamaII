from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("restoranlar", views.restoranlar),
    path("restoranlar/<slug:slug>", views.menuler, name="menuler_name")

]

#restoranlar/menu-adi