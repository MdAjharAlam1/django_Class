from django.urls import path
from main import views

urlpatterns = [
    path("",views.index,name="HomePage"),
    path("about/",views.aboutpage,name="aboutPage"),
    # path("contact/",views.contactpage,name="contactPage"),
]
