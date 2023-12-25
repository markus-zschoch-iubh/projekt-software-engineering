from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Fehlermeldung


@csrf_exempt
#@require_http_methods(["POST"])
def webhook(request):
    if request.method == 'POST':
        try:
            # Testweise den HTML Body der Nachricht schreiben
            # with open ("webhook/inbox.json" , "a") as inbox:
            #     inbox.write(str(request.body))
            #     inbox.write(str("\n"))
            
            data = json.loads(request.body)
            #Hier können Sie die empfangenen Daten verarbeiten
            #Testweise aus HTML Body extrahierte JSON Daten schreiben

            with open ("webhook/inbox.json" , "w" , encoding='utf-8') as inbox:
                json.dump(data, inbox, ensure_ascii=False, indent=4)
            print("Webhook return follows")

            fehler = Fehlermeldung.objects.create(
                matrikelnummer=data['matrikelnummer'],
                vorname=data['vorname'],
                nachname=data['nachname'],
                email=data['email'],
                kursabkuerzung=data['kursabkuerzung'],
                medium=data['medium'],
                fehlerbeschreibung=data['fehlerbeschreibung']
            )            
            
            return JsonResponse({"status": "Erfolgreich empfangen"}, status=200)
                    
        except json.JSONDecodeError:
            return JsonResponse({"error": "Ungültiges JSON"}, status=400)
    else:
        return JsonResponse({"error": "Nur POST-Methode erlaubt"}, status=405)

def fehler_list_view(request):
    fehler = Fehlermeldung.objects.all()  # Alle Einträge aus der Tabelle Fehlermeldung holen
    return render(request, 'fehlertabelle.html', {'fehler': fehler})
