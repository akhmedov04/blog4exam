from django import forms
from .models import *

class MaqolaForm(forms.ModelForm):
    class Meta:
        model = Maqola
        fields =('__all__')