from django.urls import path

from form.views import fehler_melden

urlpatterns = [path("fehler_melden", fehler_melden, name="fehler_melden")]
