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
    print(f"This Tutor: {tutor}")
    if request.method == "POST":
        zugewiesene_korrektur = Korrektur.objects.get(
            id=request.POST.get("korrektur_id", "")
        )
        print(f"Zugewiesene Korrektur: {zugewiesene_korrektur}")
        zugewiesene_korrektur.bearbeiter = tutor
        zugewiesene_korrektur.aktuellerStatus = "02"
        zugewiesene_korrektur.save()
        print(f"Zugewiesene Korrektur nach Zuweisung: {zugewiesene_korrektur}")

    offene_korrekturen = Korrektur.objects.filter(aktuellerStatus="01")
    meine_korrekturen = Korrektur.objects.filter(bearbeiter=tutor)

    return render(
        request,
        "backend/tutor-index.html",
        context={
            "korrekturen": offene_korrekturen,
            "meine_korrekturen": meine_korrekturen,
            "tutor": tutor,
        },
    )


def korrektur_bearbeiten(request, tutor_id, korrektur_id):
    tutor = Tutor.objects.get(pk=tutor_id)
    korrektur = Korrektur.objects.get(pk=korrektur_id)

    return render(
        request,
        "backend/korrektur-bearbeiten.html",
        context={"korrektur": korrektur, "tutor": tutor},
    )
