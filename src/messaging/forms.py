from django import forms
from database.models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['text']
