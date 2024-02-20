from django.urls import path

from . import views

urlpatterns = [
    path("tutor-index", views.tutor_index, name="tutor_index"),
    path(
        "korrekturen/<int:korrektur_id>",
        views.KorrekturBearbeitenView.as_view(),
        name="korrektur_bearbeiten",
    )
]
