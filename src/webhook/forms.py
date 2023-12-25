from django import forms
from webhook.models import Fehlermeldung

class FehlermeldungEditForm(forms.ModelForm):
    class Meta:
        model = Fehlermeldung
        fields = ['matrikelnummer', 'vorname', 'nachname', 'email', 'kursabkuerzung', 'medium', 'fehlerbeschreibung']
