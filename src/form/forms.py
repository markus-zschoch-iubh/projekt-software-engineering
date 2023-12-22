from django import forms

class MyForm(forms.Form):
    field1 = forms.CharField(label='Name', max_length=100)
    field2 = forms.CharField(label='Vorname', max_length=100)
    field3 = forms.CharField(label='Hier können Sie sich ausheulen:', max_length=100)
