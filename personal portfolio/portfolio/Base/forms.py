from django import forms
from .models import HireRequest

class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ['name', 'email', 'message']
