from django.urls import path
from . import views

urlpatterns = [
    path("index.html", views.index),
    path("restoranlar.html",views.restoranlar),
    path("restoranlar.html/menuler.html/<slug:slug>", views.menuler)
fygjh
]





# restoranlar/katik/zurna-doner