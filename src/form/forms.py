from django import forms

from database.models import Fehlermeldung
from database.enums import KursmaterialEnum


class FehlermeldungForm(forms.Form):
    matrikelnummer = forms.CharField(
        label="Matrikelnummer",
        max_length=100,
        initial="123456789",
    )
    vorname = forms.CharField(label="Vorname", max_length=100, initial="Max")
    nachname = forms.CharField(
        label="Nachname", max_length=100, initial="Mustermann"
    )
    email = forms.EmailField(label="Email", initial="mm@iu.de")
    kursabkuerzung = forms.CharField(
        label="Kursabkürzung", max_length=100, initial="ISSE01"
    )
    MEDIUM_CHOICES = [(choice.value, choice.label) for choice in KursmaterialEnum]

    medium = forms.ChoiceField(choices=MEDIUM_CHOICES, label="Medium")

    fehlerbeschreibung = forms.CharField(
        label="Fehlerbeschreibung",
        widget=forms.Textarea,
        initial="Bitte geben Sie hier eine möglichst genaue Fehlerbeschreibung ein.",
    )
