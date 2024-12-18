from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation

class ReservationForm(forms.ModelForm):
    COUNTRIES = [
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('GB', 'United Kingdom'),
    ('IN', 'India'),
    ('JP', 'Japan'),
    ('RU', 'Russia'),
    ('ZA', 'South Africa'),
    ('NG', 'Nigeria'),
    ('KR', 'South Korea'),
    ('CH', 'Switzerland'),
    ('PH', 'Philippines'),
    ('ID', 'Indonesia'),
    ('AE', 'United Arab Emirates'),
    ('QA', 'Qatar'),
    ('BH', 'Bahrain'),
    ('TR', 'Turkey'),
]
    
    country = forms.ChoiceField(choices=COUNTRIES)

    class Meta:
        model = Reservation
        fields = [
            'first_name', 'last_name', 'email', 'country',
            'phone', 'check_in', 'check_out', 'special_request'
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        # Validate that check-out is after check-in
        if check_in and check_out and check_out <= check_in:
            raise ValidationError("Check-out date must be after the check-in date.")

        return cleaned_data

