from django import forms
from datetime import date
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'additional_requirements']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': date.today()}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': date.today()}),
            'additional_requirements': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            self.add_error()
        return cleaned_data