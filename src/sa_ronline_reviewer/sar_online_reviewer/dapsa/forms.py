from django import forms
from .models import TestDoc


class TestDocForm(forms.Form):
    pl = forms.CharField(label="PLdoc", max_length=50)
    docfile = forms.FileField()
