from django.shortcuts import render, redirect, get_object_or_404
import requests

from form.forms import FehlermeldungForm
from database.models import Fehlermeldung


jheader = {"Content-Type": "application/json"}
webhook_url = "http://localhost:8000/webhook/"

# Funktion zum  direkten Speichern der Fehlermeldung in der DB
def fehler_melden(request):
    if request.method == 'POST':
        form = FehlermeldungForm(request.POST)
        if form.is_valid():
            Fehlermeldung.objects.create(
                matrikelnummer=form.cleaned_data['matrikelnummer'],
                vorname=form.cleaned_data['vorname'],
                nachname=form.cleaned_data['nachname'],
                email=form.cleaned_data['email'],
                kursabkuerzung=form.cleaned_data['kursabkuerzung'],
                medium=form.cleaned_data['medium'],
                fehlerbeschreibung=form.cleaned_data['fehlerbeschreibung']
            )
            return redirect('bestaetigung')

    else:
        print('!!!!!!!!!!!!!! Die Seite: "fehler_melden" wurde abgerufen !!!!!!!!!!!!!!')
        form = FehlermeldungForm()

    return render(request, "form/fehler_melden.html", {"form": form})


### Funktion zum senden der Fehlermeldung an den Webhook
def fehler_melden_an_webhook(request):
    if request.method == "POST":
        form = FehlermeldungForm(request.POST)
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
                )  # , timeout=(3,3))
                print("POST Executed")
                response.raise_for_status()

            except requests.RequestException as e:
                print("POST Error: " + str(e))

    else:
        print(
            '!!!!!!!!!!!!!! Die Seite: "fehler_melden" wurde abgerufen !!!!!!!!!!!!!!'
        )
        form = FehlermeldungForm()

    return render(request, "form/fehler_melden.html", {"form": form})


def bestaetigungsseite_view(request):
    return render(request, "form/bestaetigung.html")