from django.urls import path

from app import views
urlpatterns = [
    path("",views.index,name="HomePage"),
    path("about/",views.about,name="aboutPage"),
    path("contact/",views.contactPage,name="contactPage")
]