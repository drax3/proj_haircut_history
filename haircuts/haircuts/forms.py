from django import forms 
from .models import Haircut, Rating

class HaircutForm(forms.ModelForm):
    class Meta:
        model = Haircut
        fields = ['barber', 'shop', 'price', 'date']  # Add fields as needed


class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=10)