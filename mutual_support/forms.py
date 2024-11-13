from django import forms
from django.forms import ModelForm

from mutual_support.models import Creneau


class CreneauForm(ModelForm):
    class Meta:
        model = Creneau
        fields = ['date', 'competence', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


