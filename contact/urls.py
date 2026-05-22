from django.urls import path

from contact.views import contact, index


urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
]
