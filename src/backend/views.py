from django.shortcuts import render

# from django.http import HttpResponse

# from django.http import HttpResponse

from database.models import Korrektur, Tutor

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
