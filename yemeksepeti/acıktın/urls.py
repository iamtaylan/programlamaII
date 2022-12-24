from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("restoranlar", views.restoranlar, name="restoran_page"),
    path("restoranlar/<slug:slug>", views.menuler, name="menuler_name")

]

#restoranlar/menu-adi