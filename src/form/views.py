import http.client
import json
from urllib import parse
from urllib import request as nrequest

import requests
from django.http import JsonResponse
from django.shortcuts import render

from form.forms import FehlermeldungForm

### ORIGINAL MIT TIMEOUT FEHLER

# def fehler_melden(request):
#     if request.method == 'POST':
#         form = FehlermeldungForm(request.POST)
#         if form.is_valid():
#             # Konvertieren der Formulardaten in ein Python-Dict
#             form_data = form.cleaned_data

#             # Konvertieren der Daten in JSON und Senden an den Webhook
#             try:
#                 with open ("form/sendmsg.json" , "w" , encoding='utf-8') as sendmsg:
#                     json.dump(form_data, sendmsg, ensure_ascii=False, indent=4)
#                 print("sendmsg written")
#                 headers = {'Content-Type': 'application/json'}
#                 response = requests.post('http://localhost:8000/webhook/', json=form_data, headers=headers, timeout=(3,3))
#                 print("POST Executed")
#                 response.raise_for_status()

#             except requests.RequestException as e:
#                 # Hier können Sie Fehlerbehandlung einfügen, falls nötig
#                 print("POST Error " + str(e))

#     else:
#         print('!' * 200)
#         form = FehlermeldungForm()

#     return render(request, 'my_template.html', {'form': form})

jheader = {"Content-Type": "application/json"}
webhook_host = "localhost:8000"
webhook_path = "/webhook"
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
                    "http://localhost:8000/webhook/",
                    json=form_data,
                    headers=jheader,
                )  # , timeout=(3,3))
                print("POST Executed")
                response.raise_for_status()

                ### VERSUCH MIT hhtp.client ### FÜHRT ZUM GLEICHEN WORKER TIMEOUT WIE REQUESTS

                # # Erstellen einer Verbindung und Senden der Anfrage
                # conn = http.client.HTTPSConnection(webhook_host)
                # headers = {'Content-type': 'application/json'}
                # conn.request("POST", webhook_path, form_data, headers)

                # # Empfangen der Antwort
                # response = conn.getresponse()

                # # Überprüfung des Statuscodes
                # if response.status == 200:
                #     return JsonResponse({'message': 'Erfolg! Nachricht erfolgreich gesendet.'})
                # else:
                #     return JsonResponse({'message': 'Fehler! Nachricht konnte nicht gesendet werden.'}, status=500)

            except requests.RequestException as e:
                print("POST Error: " + str(e))

    else:
        print(
            '!!!!!!!!!!!!!! Die Seite: "fehler_melden" wurde abgerufen !!!!!!!!!!!!!!'
        )
        form = FehlermeldungForm()

    return render(request, "my_template.html", {"form": form})
