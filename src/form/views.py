from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests

from form.forms import KorrekturForm
from database.models import Korrektur, Student, Kurs


jheader = {"Content-Type": "application/json"}
webhook_url = "http://localhost:8000/webhook/"


# Funktion zum  direkten Speichern der Fehlermeldung in der DB
@login_required
def fehler_melden(request):
    if request.method == "POST":
        form = KorrekturForm(request.POST)
        if form.is_valid():
            user = request.user
            email = user.email
            kurs_id = form.cleaned_data["kurs"]
            kurs_objekt = Kurs.objects.get(kurzname=kurs_id)

            try:
                # Den Studenten anhand der E-Mail finden
                student = Student.objects.get(email=email)
                # Matrikelnummer des Studenten erhalten
                matrikelnummer = student.martrikelnummer
                # Den Studenten als Objekt anhand der Matrikelnummer finden
                ersteller_student = Student.objects.get(
                    martrikelnummer=matrikelnummer
                )
            except Student.DoesNotExist:
                # Behandlung, falls kein Student mit dieser E-Mail existiert
                matrikelnummer = None
                # Hier vielleicht noch auf eine Ups da ist was schief gelaufen Seite weiterleiten
                return render(
                    request, "form/fehler_melden.html", {"form": form}
                )

            Korrektur.objects.create(
                ersteller=ersteller_student,
                typ=form.cleaned_data["typ"],
                kurs=kurs_objekt,
                fehler_beschreibung=form.cleaned_data["fehler_beschreibung"],
            )
            return redirect("bestaetigung")

    else:
        print(
            '!!!!!!!!!!!!!! Die Seite: "fehler_melden" wurde abgerufen !!!!!!!!!!!!!!'
        )
        form = KorrekturForm()

    return render(request, "form/fehler_melden.html", {"form": form})


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


def bestaetigungsseite_view(request):
    return render(request, "form/bestaetigung.html")
