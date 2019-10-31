from django import forms
from .models import Flight


class SearchForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('airline', 'airport', 'arrived', 'date')
