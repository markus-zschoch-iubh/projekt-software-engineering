from django.urls import path

from form.views import fehler_melden, bestaetigungsseite_view

urlpatterns = [
    path("fehler_melden", fehler_melden, name="fehler_melden"),
    path("bestaetigung/", bestaetigungsseite_view, name="bestaetigung"),
]
