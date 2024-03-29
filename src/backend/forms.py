from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from database.models import Korrektur, Messages


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