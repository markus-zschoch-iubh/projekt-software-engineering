from django import forms

from database.models import Kursmaterial, Korrektur


class KorrekturForm(forms.ModelForm):
    """
    A form for creating a Korrektur object.
    """

    class Meta:
        """
            Meta class for defining metadata options for the form.
        """
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
        """
        Initialize the form instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.fields["kursmaterial"].queryset = Kursmaterial.objects.none()

        if "kurs" in self.data:
            kurs_id = int(self.data.get("kurs"))
            self.fields["kursmaterial"].queryset = Kursmaterial.objects.filter(
                kurs_id=kurs_id
            )
