from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from form.forms import KorrekturForm
from database.models import Kursmaterial, Messages
from messaging.helper import ersteller_message_bei_neuer_korrektur
from messaging.views import get_student


# Create your views here.


class FehlerMeldenView(View):
    """
    View class for reporting errors.
    """

    form_class = KorrekturForm
    initial = {"key": "value"}
    template_name = "form/fehler_melden.html"

    @method_decorator(login_required)
    def get(self, request):
        """
        Handles GET requests for the FehlerMeldenView.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        student = get_student(request)
        print(student)
        if not student:
            return redirect("/accounts/login")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    @method_decorator(login_required)
    def post(self, request):
        """
        Handles POST requests for the FehlerMeldenView.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        form = self.form_class(request.POST)

        if form.is_valid():
            ersteller_student = get_student(request)
            korrektur = form.save(commit=False)
            korrektur.ersteller = ersteller_student
            korrektur.save()
            ersteller_message_bei_neuer_korrektur(korrektur, ersteller_student)
            return redirect("bestaetigung")

        return render(request, self.template_name, {"form": form})


def bestaetigungsseite_view(request):
    """
    Renders the bestaetigung.html template and returns the rendered HTML as a response.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML response.
    """
    return render(request, "form/bestaetigung.html")


def load_kursmaterialien(request):
    """
    Load kursmaterialien based on the provided kurs_id.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the kursmaterialien options.
    """
    kurs_id = request.GET.get("kurs")
    kursmaterialien = Kursmaterial.objects.filter(kurs_id=kurs_id)
    return render(
        request,
        "form/kursmaterial_options.html",
        {"kursmaterialien": kursmaterialien},
    )
