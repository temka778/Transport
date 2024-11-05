from django import forms
from django.utils import timezone
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'additional_requirements']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
            'additional_requirements': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and start_date < timezone.now().date():
            self.add_error('start_date', "Дата начала аренды не может быть раньше сегодняшнего дня.")
        if end_date and end_date < start_date:
            self.add_error('end_date', "Дата окончания аренды не может быть раньше даты начала аренды.")

        return cleaned_data