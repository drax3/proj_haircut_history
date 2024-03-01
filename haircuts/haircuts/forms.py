from django import forms 
from .models import Haircut

class HaircutForm(forms.ModelForm):
    class Meta:
        model = Haircut
        fields = ['barber', 'shop', 'price', 'date']  # Add fields as needed

