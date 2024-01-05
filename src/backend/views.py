from django.shortcuts import render, get_object_or_404, redirect

# from django.http import HttpResponse

# from django.http import HttpResponse

from database.models import Korrektur, Tutor, Fehlermeldung
from backend.forms import FehlermeldungEditForm

# Create your views here.


def tutor_overview(request):
    tutoren = Tutor.objects.all()

    return render(
        request, "backend/overview.html", context={"tutoren": tutoren}
    )


def tutor_index(request, tutor_id):
    tutor = Tutor.objects.get(pk=tutor_id)
    offene_korrekturen = Korrektur.objects.filter(aktuellerStatus="01")
    meine_korrekturen = Korrektur.objects.filter(bearbeiter=tutor)

    return render(
        request,
        "backend/tutor_index.html",
        context={
            "korrekturen": offene_korrekturen,
            "meine_korrekturen": meine_korrekturen,
        },
    )


def fehler_list_view(request):
    fehler = (
        Fehlermeldung.objects.all()
    )  # Alle Einträge aus der Tabelle Fehlermeldung holen
    return render(request, "backend/fehlerliste.html", {"fehler": fehler})


def fehler_edit_view(request, id):
    fehler = get_object_or_404(Fehlermeldung, id=id)
    if request.method == "POST":
        form = FehlermeldungEditForm(request.POST, instance=fehler)
        if form.is_valid():
            form.save()
            return redirect("fehlerliste")
    else:
        form = FehlermeldungEditForm(instance=fehler)
    return render(request, "backend/fehler_edit.html", {"form": form})
