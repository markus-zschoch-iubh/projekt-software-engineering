from django.shortcuts import render
import requests

from form.forms import FehlermeldungForm


jheader = {"Content-Type": "application/json"}
webhook_url = "http://localhost:8000/webhook/"


def fehler_melden(request):
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
