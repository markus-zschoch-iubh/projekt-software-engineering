from django import forms

from database.models import Kursmaterial, Korrektur


class KorrekturForm(forms.ModelForm):
    class Meta:
        model = Korrektur
        fields = ["kurs", "kursmaterial", "beschreibung"]
        # Optional: Widgets hinzufügen, um die Darstellung der Formularfelder zu ändern
        widgets = {
            "beschreibung": forms.Textarea(attrs={"cols": 50, "rows": 10}),
            "kurs": forms.Select(
                attrs={
                    "hx-get": "load_kursmaterialien/",
                    "hx-target": "#id_kursmaterial",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["kursmaterial"].queryset = Kursmaterial.objects.none()

        if "kurs" in self.data:
            kurs_id = int(self.data.get("kurs"))
            self.fields["kursmaterial"].queryset = Kursmaterial.objects.filter(
                kurs_id=kurs_id
            )
