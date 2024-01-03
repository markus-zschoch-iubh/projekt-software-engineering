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
    korrekturen = Korrektur.objects.all()

    return render(
        request,
        "backend/tutor_index.html",
        context={"korrekturen": korrekturen},
    )
