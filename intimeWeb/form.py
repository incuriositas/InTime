from django import forms
from .models import Flight
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput


class SearchForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('airline', 'airport', 'arrived', 'date')
        widgets = {
            'date': DateTimePickerInput()
        }
