from django import forms
from .models import ReservationForm

class ReservationFormForm(forms.ModelForm):
    class Meta:
        model = ReservationForm
        fields = '__all__'
