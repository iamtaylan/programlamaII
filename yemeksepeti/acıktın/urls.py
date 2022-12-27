from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("account/", include("account.urls"), name="profil"),
    path("restoranlar", views.restoranlar, name="restoran_page"),
    path("restoranlar/<slug:slug>", views.menuler, name="menuler_name")

]

#restoranlar/menu-adi