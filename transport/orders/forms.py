from django import forms
from django.utils import timezone
from zoneinfo import ZoneInfo
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['start_date', 'end_date', 'additional_requirements']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_date = timezone.now().astimezone(ZoneInfo('Europe/Samara')).date().isoformat()
        self.fields['start_date'].widget = forms.DateInput(
            attrs={'type': 'date', 'min': current_date}
        )
        self.fields['end_date'].widget = forms.DateInput(
            attrs={'type': 'date', 'min': current_date}
        )
        self.fields['additional_requirements'].widget = forms.Textarea(attrs={'rows': 3})

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        current_datetime = timezone.now().astimezone(ZoneInfo('Europe/Samara')).date()
        if start_date and start_date < current_datetime:
            self.add_error('start_date', "Дата начала аренды не может быть раньше сегодняшнего дня.")
        if end_date and start_date and end_date < start_date:
            self.add_error('end_date', "Дата окончания аренды не может быть раньше даты начала аренды.")
        return cleaned_data