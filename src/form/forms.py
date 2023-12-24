from django import forms

class FehlermeldungForm(forms.Form):
    matrikelnummer = forms.CharField(label='Matrikelnummer', max_length=100, initial='123456789',)
    vorname = forms.CharField(label='Vorname', max_length=100, initial='Max')
    nachname = forms.CharField(label='Nachname', max_length=100, initial='Mustermann')
    email = forms.EmailField(label='Email', initial='mm@iu.de')
    kursabkuerzung = forms.CharField(label='Kursabkürzung', max_length=100, initial='ISSE01')
    medium = forms.CharField(label='Medium', max_length=100, initial='Gedrucktes Skript')
    fehlerbeschreibung = forms.CharField(label='Fehlerbeschreibung', widget=forms.Textarea, initial='Fehlerbeschreibung')

