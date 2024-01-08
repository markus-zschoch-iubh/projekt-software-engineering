import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from database.models import Korrektur


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    if request.method == "POST":
        print("WEBHOOK ERKENNT POST")
        try:
            data = json.loads(request.body)
            
            # Testweise aus HTML Body extrahierte JSON Daten schreiben
            with open("webhook/inbox.json", "w", encoding="utf-8") as inbox:
                json.dump(data, inbox, ensure_ascii=False, indent=4)

            print("Webhook return follows")

            Korrektur.objects.create(
                ersteller=data["ersteller"],
                typ=data["typ"],
                kurs=data["kurs"],
                fehler_beschreibung=data["fehler_beschreibung"]
            )

            print("Neue Meldung beim Webhook eingegangen: " + str(data))

            return JsonResponse({"status": "Erfolgreich empfangen"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Ungültiges JSON"}, status=400)
    else:
        return JsonResponse({"error": "Nur POST-Methode erlaubt"}, status=405)