from django import forms
from database.models import Messages


class MessageForm(forms.ModelForm):
    """
    A form for creating a new message.

    This form is used to create a new message by providing a text input field.

    """

    class Meta:
        model = Messages
        fields = ["text"]
        labels = {"text": "Neue Nachricht"}
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "placeholder": """Gib hier deine
                    Nachricht an den Tutor ein.""",
                    "rows": 2,
                }
            ),
        }
