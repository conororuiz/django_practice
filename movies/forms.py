from movies.models import *
from  django.core.exceptions import ValidationError
from django import forms

class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie
        fields='__all__'

class MovieRateForm(forms.ModelForm):

    class Meta:
        model=MovieRate
        fields='__all__'
