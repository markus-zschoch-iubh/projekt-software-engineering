from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
   return HttpResponse("Hier entsteht das Formular zur Korrekturmedlung.")

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Testweise den HTML Body der Nachricht schreiben
            # with open ("webhook/inbox.json" , "a") as inbox:
            #     inbox.write(str(request.body))
            #     inbox.write(str("\n"))
            
            data = json.loads(request.body)
            # Hier können Sie die empfangenen Daten verarbeiten
            # Testweise aus HTML Body extrahierte JSON Daten schreiben
            #with open ("webhook/inbox.json" , "a") as inbox:
            #    inbox.write(str(data))
            with open ("webhook/inbox.json" , "w" , encoding='utf-8') as inbox:
                json.dump(data, inbox, ensure_ascii=False, indent=4)
            print("Webhook return follows")
            return JsonResponse({"status": "Erfolgreich empfangen"}, status=200)
            #return HttpResponse(status=200)
            
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Ungültiges JSON"}, status=400)
    else:
        return JsonResponse({"error": "Nur POST-Methode erlaubt"}, status=405)
