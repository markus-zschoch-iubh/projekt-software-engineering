from django.urls import path

from pages import views

urlpatterns = [
    path("", views.welcome_page, name="welcome_page"),
]
