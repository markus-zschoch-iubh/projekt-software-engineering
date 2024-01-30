from django import forms
from database.models import Messages

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Messages
#         fields = ['text']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',  # Bootstrap-Klasse für Stil
                'placeholder': 'Geben Sie Ihre Nachricht ein',  # Platzhaltertext
                'rows': 2,  # Höhe des Textfeldes
            }),
        }
