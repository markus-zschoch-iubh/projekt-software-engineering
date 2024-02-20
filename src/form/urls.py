from django.urls import path

from . import views

urlpatterns = [
    path(
        "fehler_melden", views.FehlerMeldenView.as_view(), name="fehler_melden"
    ),
    path("bestaetigung/", views.bestaetigungsseite_view, name="bestaetigung"),
    path(
        "load_kursmaterialien/",
        views.load_kursmaterialien,
        name="load_kursmaterialien",
    ),
]
