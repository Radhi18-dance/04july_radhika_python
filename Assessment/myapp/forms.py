from django import forms
from .models import *
class signupForm(forms.ModelForm):
    class Meta:
        model=signmodel
        fields='__all__'
class updatepassForm(forms.ModelForm):
    class Meta:
        model=signmodel
        fields=['password']

class registerForm(forms.ModelForm):
    class Meta:
        model=event
        fields='__all__'

class updateform(forms.ModelForm):
    class Meta:
        model=signmodel
        fields=['fullname','mobile','email','password']



        