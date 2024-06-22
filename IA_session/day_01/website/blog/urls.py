from django.urls import path
from . import views

urlpatterns = [
    path("list/",views.bloglist),
    path("list/<int:id>/",views.blogdetail)
]
