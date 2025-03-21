from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model=signmodel
        fields='__all__'