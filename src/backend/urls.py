from django.urls import path

from . import views

urlpatterns = [
    path("tutor_index", views.tutor_index, name="tutor_index"),
    path(
        "<int:korrektur_id>",
        views.korrektur_bearbeiten,
        name="korrektur_bearbeiten",
    ),
    path("fehlerliste/", views.fehler_list_view, name="fehlerliste"),
]
