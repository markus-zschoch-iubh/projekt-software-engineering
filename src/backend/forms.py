from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from database.models import Korrektur, Messages


class MessagesForm(forms.ModelForm):
    
    class Meta:
        model = Messages
        fields = ("tutor", "status", "text")
        widgets = {
            "text": forms.Textarea(attrs={"cols": 50, "rows": 10}),
        }