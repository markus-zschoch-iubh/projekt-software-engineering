from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .forms import MessagesForm
from database.models import Korrektur, Messages, Tutor


# Helper functions


def get_tutor(request):
    try:
        tutor = Tutor.objects.get(email=request.user.email)

    except Exception as e:
        print(e)
        tutor = None

    return tutor


# Create your views here.


class KorrekturBearbeitenView(View):
    form_class = MessagesForm
    initial = {"key": "value"}
    template_name = "backend/korrektur-bearbeiten.html"

    @method_decorator(login_required)
    def get(self, request, korrektur_id):
        tutor = get_tutor(request)
        if tutor is None:
            return HttpResponseForbidden(
                "Ein Tutor mit dieser Emailadresse existiert nicht."
            )

        korrektur = Korrektur.objects.get(pk=korrektur_id)
        korrektur.aktuellerStatus = korrektur.get_aktuellerStatus_display()

        messages = Messages.objects.filter(korrektur=korrektur).order_by(
            "created_at"
        )
        for message in messages:
            message.status = message.get_status_display()
            # message.sender = message.get_sender_display()

        form = self.form_class(initial=self.initial)

        return render(
            request,
            self.template_name,
            context={
                "form": form,
                "korrektur": korrektur,
                "tutor": tutor,
                "messages": messages,
            },
        )

    @method_decorator(login_required)
    def post(self, request, korrektur_id):
        tutor = get_tutor(request)
        if tutor is None:
            return HttpResponseForbidden(
                "Ein Tutor mit dieser Emailadresse existiert nicht."
            )

        korrektur = Korrektur.objects.get(pk=korrektur_id)
        korrektur.aktuellerStatus = korrektur.get_aktuellerStatus_display()

        form = self.form_class(request.POST)

        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.student = korrektur.ersteller
            new_message.korrektur = korrektur
            new_message.sender = "01"
            new_message.aenderungTyp = "04"
            if new_message.tutor is not korrektur.bearbeiter:
                new_message.aenderungTyp = "02"
                korrektur.bearbeiter = new_message.tutor
            if new_message.status is not korrektur.aktuellerStatus:
                new_message.aenderungTyp = "03"
                korrektur.aktuellerStatus = new_message.status
            new_message.save()
            korrektur.save()
            return redirect("/backend/tutor-index")

        messages = Messages.objects.filter(korrektur=korrektur).order_by(
            "created_at"
        )

        return render(
            request,
            self.template_name,
            context={
                "form": form,
                "korrektur": korrektur,
                "tutor": tutor,
                "messages": messages,
            },
        )


@login_required
def korrektur_bearbeiten(request, korrektur_id):
    tutor = get_tutor(request)
    if tutor is None:
        return HttpResponseForbidden(
            "Ein Tutor mit dieser Emailadresse existiert nicht."
        )

    korrektur = Korrektur.objects.get(pk=korrektur_id)
    korrektur.aktuellerStatus = korrektur.get_aktuellerStatus_display()

    messages = Messages.objects.filter(korrektur=korrektur)

    return render(
        request,
        "backend/korrektur-bearbeiten.html",
        context={"korrektur": korrektur, "tutor": tutor, "messages": messages},
    )


@login_required
def tutor_index(request):
    tutor = get_tutor(request)
    if tutor is None:
        return HttpResponseForbidden(
            "Ein Tutor mit dieser Emailadresse existiert nicht."
        )

    if request.method == "POST" and request.POST.get("korrektur_id", ""):
        zugewiesene_korrektur = Korrektur.objects.get(
            id=request.POST.get("korrektur_id", "")
        )
        zugewiesene_korrektur.bearbeiter = tutor
        zugewiesene_korrektur.aktuellerStatus = "02"
        zugewiesene_korrektur.save()

    offene_korrekturen = Korrektur.objects.filter(aktuellerStatus="01")
    for korrektur in offene_korrekturen:
        # korrektur.kursmaterial = korrektur.get_kursmaterial_display()
        korrektur.aktuellerStatus = korrektur.get_aktuellerStatus_display()
    meine_korrekturen = Korrektur.objects.filter(bearbeiter=tutor)
    for korrektur in meine_korrekturen:
        # korrektur.kursmaterial = korrektur.get_kursmaterial_display()
        korrektur.aktuellerStatus = korrektur.get_aktuellerStatus_display()

    return render(
        request,
        "backend/tutor-index.html",
        context={
            "korrekturen": offene_korrekturen,
            "meine_korrekturen": meine_korrekturen,
            "tutor": tutor,
        },
    )


def fehler_list_view(request):
    fehler = (
        Korrektur.objects.all()
    )  # Alle Einträge aus der Tabelle Fehlermeldung holen
    return render(request, "backend/fehlerliste.html", {"fehler": fehler})
