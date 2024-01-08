from django import forms

from database.enums import KursmaterialEnum
from database.models import Kurs, Student


class KorrekturForm(forms.Form):
    typ_choices = [(choice.value, choice.label) for choice in KursmaterialEnum]
    typ = forms.ChoiceField(choices=typ_choices, label="Art des Kursmaterials")

#    Wird eigentlich nciht gebraucht, da der eingeloggte Student 
#    automatisch erkannt wird
#    ersteller = forms.CharField(
#        label="Matrikelnummer",
#        max_length=20,
#        initial="222222222",
#    )

   
    kurs_choices = [(choice.kurzname, choice.name) for choice in Kurs.objects.all()]
    kurs = forms.ChoiceField(choices=kurs_choices, label="Kurs")
    
    fehler_beschreibung = forms.CharField(
        label="Fehlerbeschreibung",
        widget=forms.Textarea,
        initial="Bitte geben Sie hier eine möglichst genaue Fehlerbeschreibung ein.",
    )
