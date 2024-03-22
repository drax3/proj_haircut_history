from django import forms 
from .models import Haircut, Rating
from datetime import datetime

class HaircutForm(forms.ModelForm):
    class Meta:
        model = Haircut
        fields = ['barber', 'shop', 'price', 'date', 'cutside1','cutside2','cutside3']  # Add fields as needed

        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].initial = datetime.date.today()  # Set initial value to today's date


class RatingForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=10)