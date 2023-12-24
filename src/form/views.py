from django.shortcuts import render
from django.http import HttpResponse
from .forms import FehlermeldungForm
import json

# Create your views here.
#def index(request):
#    return HttpResponse("Hier entsteht das Formular zur Korrekturmedlung.")


# Create your views here.
# def index(request):
    
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             # Hier können Sie die validierten Daten verarbeiten
#             pass
#     else:
#         form = MyForm()

#     return render(request, 'my_template.html', {'form': form})

import requests

def index(request):
    if request.method == 'POST':
        form = FehlermeldungForm(request.POST)
        if form.is_valid():
            # Konvertieren der Formulardaten in ein Python-Dict
            form_data = form.cleaned_data

            # Konvertieren der Daten in JSON und Senden an den Webhook
            try:
                with open ("form/sendmsg.json" , "w" , encoding='utf-8') as sendmsg:
                    json.dump(form_data, sendmsg, ensure_ascii=False, indent=4)
                print("sendmsg written")
                headers = {'Content-Type': 'application/json'}
                response = requests.post('http://localhost:8000/webhook/', json=form_data, headers=headers, timeout=(3,3))
                print("POST Executed")
                response.raise_for_status()
                
            except requests.RequestException as e:
                # Hier können Sie Fehlerbehandlung einfügen, falls nötig
                print("POST Error " + str(e))

    else:
        form = FehlermeldungForm()

    return render(request, 'my_template.html', {'form': form})

