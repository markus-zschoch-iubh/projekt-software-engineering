from django import forms

from database.models import Messages


class MessagesForm(forms.ModelForm):
    """
    A form for creating or updating Messages.

    This form is used to create or update Messages objects in the database.
    It includes fields for the tutor, status, and text of the message.

    Attributes:
        tutor (ForeignKey): The tutor associated with the message.
        status (CharField): The status of the message.
        text (CharField): The text content of the message.
    """

    class Meta:
        model = Messages
        fields = ("tutor", "status", "text")
        widgets = {
            "text": forms.Textarea(attrs={"cols": 50, "rows": 10}),
        }
