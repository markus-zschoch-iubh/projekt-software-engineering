from django.http import HttpResponse
from django.shortcuts import render

from webhook.models import Fehlermeldung

# Create your views here.
def index(request):
    return HttpResponse("Hier entsteht das Backend für Tutoren.")


def student_overview(request, matrikelnummer):
    fehlermeldungen = Fehlermeldung.objects.filter(matrikelnummer=matrikelnummer)
    return render(request, 'fehler_student.html', {'fehlermeldungen': fehlermeldungen})

