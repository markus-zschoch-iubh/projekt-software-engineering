from django.urls import path

from . import views

urlpatterns = [
    path("", views.tutor_overview, name="tutor_overview"),
    path("<int:tutor_id>", views.tutor_index, name="tutor_index"),
    path("fehlerliste/", views.fehler_list_view, name="fehlerliste")
]
