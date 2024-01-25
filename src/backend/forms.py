from django import forms

from database.models import Messages

class MessagesForm(forms.ModelForm):
    
    class Meta:
        model = Messages
        fields = ("tutor", "status", "text")
        widgets = {
            "text": forms.Textarea(attrs={"cols": 50, "rows": 10}),
         }
