from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
#import requests

from form.forms import KorrekturForm
from database.models import Kursmaterial, Messages
from messaging.helper import ersteller_message_bei_neuer_korrektur
from messaging.views import get_student


jheader = {"Content-Type": "application/json"}
webhook_url = "http://localhost:8000/webhook/"

# Create your views here.


class FehlerMeldenView(View):
    form_class = KorrekturForm
    initial = {"key": "value"}
    template_name = "form/fehler_melden.html"

    @method_decorator(login_required)
    def get(self, request):
        student = get_student(request)
        print(student)
        if not student:
            return redirect("/accounts/login")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    @method_decorator(login_required)
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            ersteller_student = get_student(request)
            korrektur = form.save(commit=False)
            korrektur.ersteller = ersteller_student
            korrektur.save()
            ersteller_message_bei_neuer_korrektur(korrektur, ersteller_student)
            return redirect("bestaetigung")

        return render(request, self.template_name, {"form": form})


"""@login_required
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
    return render(request, "form/fehler_melden.html", {"form": form})"""


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


def load_kursmaterialien(request):
    kurs_id = request.GET.get("kurs")
    kursmaterialien = Kursmaterial.objects.filter(kurs_id=kurs_id)
    return render(
        request,
        "form/kursmaterial_options.html",
        {"kursmaterialien": kursmaterialien},
    )
