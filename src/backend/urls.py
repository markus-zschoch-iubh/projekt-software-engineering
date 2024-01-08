from django.urls import path

from . import views

urlpatterns = [
    path("", views.tutor_overview, name="tutor_overview"),
    path("<int:tutor_id>", views.tutor_index, name="tutor_index"),
    path(
        "<int:tutor_id>/<int:korrektur_id>",
        views.korrektur_bearbeiten,
        name="korrektur_bearbeiten",
    ),
]
