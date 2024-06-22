from django.urls import path
from app import views

urlpatterns = [
    path("",views.index,name="HomePage"),
    path("reverse_pgm/",views.reverse_pgm,name="about")
]
