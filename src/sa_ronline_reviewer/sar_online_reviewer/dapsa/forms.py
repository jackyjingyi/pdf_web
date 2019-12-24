from django import forms
from .models import Document, TestDoc


class DocumentForm(forms.Form):
    description = forms.CharField(max_length=255)
    pl = forms.CharField(max_length=255)
    upload = forms.FileField(label='Select a file',
                               help_text='max. 42 megabytes')

class TestDocForm(forms.Form):
    docfile = forms.FileField(label='Select a file',
                              help_text='max. 42 megabytes'
                              )
