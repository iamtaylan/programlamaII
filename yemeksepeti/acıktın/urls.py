from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("restoranlar", views.restoranlar, name="restoran_page"),
    path("blank", views.blank, name="blank_page"),
    path("restoranlar/tum-menuler", views.tumMenuler, name="tum_menuler_page"),
    path("restoranlar/tum-menuler/", views.tumMenuler, name="tum_menuler_page"),
    path("restoranlar/tum-menuler/<slug:slug>", views.menuler, name="menuler_name")

]

#restoranlar/menu-adi