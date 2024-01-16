from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests

from form.forms import KorrekturForm
from database.models import Korrektur, Student, Kurs, Kursmaterial
from messaging.views import get_student


jheader = {"Content-Type": "application/json"}
webhook_url = "http://localhost:8000/webhook/"

# Create your views here.


@login_required
def fehler_melden(request):
    form = KorrekturForm(request.POST)
    if request.method == "POST":
        print('---- Die Seite: "fehler_melden" hat einen POST gesendet ----')
        if form.is_valid():
            korrektur = form.save(
                commit=False
            )  # Erstellt ein Korrektur-Objekt, speichert es aber noch nicht in der Datenbank
            korrektur.ersteller = get_student(
                request
            )  # Setzt den aktuellen Benutzer als Ersteller
            korrektur.save()  # Speichert das Objekt in der Datenbank
            return redirect("bestaetigung")
    else:
        print('---- Die Seite: "fehler_melden" wurde abgerufen ----')
    form = KorrekturForm()
    return render(request, "form/fehler_melden.html", {"form": form})


def bestaetigungsseite_view(request):
    return render(request, "form/bestaetigung.html")


### Funktion zum senden der Fehlermeldung an den Webhook - Funktioniert nicht mehr ###
def fehler_melden_an_webhook(request):
    if request.method == "POST":
        form = KorrekturForm(request.POST)
        if form.is_valid():
            # Konvertieren der Formulardaten in ein Python-Dict
            form_data = form.cleaned_data
            print(str(form_data))
            # Senden an den Webhook
            try:
                ### VERSUCH MIT REQUESTS ###
                print("JETZT FOLGT DER POST DER ZUM WORKER ABSTURZ FUEHRT")
                response = requests.post(
                    webhook_url,
                    json=form_data,
                    headers=jheader,
                    timeout=(3, 3),
                )
                print("POST Executed")
                response.raise_for_status()

            except requests.RequestException as e:
                print("POST Error: " + str(e))

    else:
        print(
            '!!!!!!!!!!!!!! Die Seite: "fehler_melden" wurde abgerufen !!!!!!!!!!!!!!'
        )
        form = KorrekturForm()

    return render(request, "form/fehler_melden.html", {"form": form})


# AJAX
def load_kursmaterialien(request):
    kurs_id = request.GET.get("kurs_id")
    kursmaterialien = Kursmaterial.objects.filter(kurs_id=kurs_id).all()
    return render(
        request,
        "form/kursmaterial_dropdown_list_options.html",
        {"kursmaterialien": kursmaterialien},
    )
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
