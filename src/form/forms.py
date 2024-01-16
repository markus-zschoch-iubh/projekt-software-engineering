from django import forms

from database.models import Kursmaterial, Korrektur


# class KorrekturForm(forms.Form):
#     typ_choices = [(choice.value, choice.label) for choice in KursmaterialEnum]
#     typ = forms.ChoiceField(choices=typ_choices, label="Art des Kursmaterials")
#     kurs_choices = [
#         (choice.kurzname, choice.name) for choice in Kurs.objects.all()
#     ]
#     kurs = forms.ChoiceField(choices=kurs_choices, label="Kurs")
#     fehler_beschreibung = forms.CharField(
#         label="Fehlerbeschreibung",
#         widget=forms.Textarea,
#         initial="Bitte geben Sie hier eine möglichst genaue Fehlerbeschreibung ein.",
#     )


class KorrekturForm(forms.ModelForm):
    class Meta:
        model = Korrektur
        fields = ["kurs", "kursmaterial", "beschreibung"]
        # Optional: Widgets hinzufügen, um die Darstellung der Formularfelder zu ändern
        widgets = {
            "beschreibung": forms.Textarea(attrs={"cols": 50, "rows": 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["kursmaterial"].queryset = Kursmaterial.objects.none()

        if "kurs" in self.data:
            try:
                kurs_id = int(self.data.get("kurs"))
                self.fields[
                    "kursmaterial"
                ].queryset = Kursmaterial.objects.filter(kurs_id=kurs_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields[
                "kursmaterial"
            ].queryset = self.instance.kurs.kursmaterial_set
