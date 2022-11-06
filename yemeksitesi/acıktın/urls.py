from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index),
    path("restoranlar",views.restoranlar),
    path("restoranlar/menuler/<slug:slug>", views.menuler)

]





# restoranlar/katik/zurna-doner