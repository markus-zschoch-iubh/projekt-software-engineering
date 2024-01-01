import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from webhook.forms import FehlermeldungEditForm
from webhook.models import Fehlermeldung


@csrf_exempt
# @require_http_methods(["POST"])
def webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # Hier können Sie die empfangenen Daten verarbeiten
            # Testweise aus HTML Body extrahierte JSON Daten schreiben

            with open("webhook/inbox.json", "w", encoding="utf-8") as inbox:
                json.dump(data, inbox, ensure_ascii=False, indent=4)
            print("Webhook return follows")

            neue_meldung = Fehlermeldung.objects.create(
                # id=data['id'],
                matrikelnummer=data["matrikelnummer"],
                vorname=data["vorname"],
                nachname=data["nachname"],
                email=data["email"],
                kursabkuerzung=data["kursabkuerzung"],
                medium=data["medium"],
                fehlerbeschreibung=data["fehlerbeschreibung"],
            )

            return redirect("bestaetigungsseite", id=neue_meldung.id)
            # return JsonResponse({"status": "Erfolgreich empfangen"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Ungültiges JSON"}, status=400)
    else:
        return JsonResponse({"error": "Nur POST-Methode erlaubt"}, status=405)


def fehler_list_view(request):
    fehler = (
        Fehlermeldung.objects.all()
    )  # Alle Einträge aus der Tabelle Fehlermeldung holen
    return render(request, "fehlertabelle.html", {"fehler": fehler})


def fehler_edit_view(request, id):
    fehler = get_object_or_404(Fehlermeldung, id=id)
    if request.method == "POST":
        form = FehlermeldungEditForm(request.POST, instance=fehler)
        if form.is_valid():
            form.save()
            return redirect("fehlerliste")
    else:
        form = FehlermeldungEditForm(instance=fehler)
    return render(request, "fehler_edit.html", {"form": form})


def bestaetigungsseite_view(request, id):
    fehler = get_object_or_404(Fehlermeldung, id=id)
    return render(request, "bestaetigung.html", {"fehler": fehler})
