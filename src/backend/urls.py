from django.urls import path

from .views import index, student_overview


urlpatterns = [
    path("", index),
    path('student/<str:matrikelnummer>/', student_overview, name='fehler_student'),
]

