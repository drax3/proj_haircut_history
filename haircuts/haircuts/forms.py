# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms 
from .models import Haircut, Rating
from datetime import datetime

class HaircutForm(forms.ModelForm):
    class Meta:
        model = Haircut
        fields = ['barber', 'shop', 'price', 'date', 'cutside1','cutside2','cutside3']
        # fields = '__all__'  
    # def save(self, commit=True, user=None):
    #     instance = super().save(commit=False)
    #     if user:
    #         instance.person = user
    #     if commit:
    #         instance.save()
    #     return instance
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.person = user
        elif hasattr(self, 'request') and hasattr(self.request, 'user'):
            instance.person = self.request.user
        if commit:
            instance.save()
        return instance

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.form_class = 'form-horizontal'
    #     self.helper.label_class = 'col-sm-2 control-label'
    #     self.helper.field_class = 'col-sm-10'
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('barber', css_class='form-group col-md-6 mb-0'),
    #             Column('shop', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('price', css_class='form-group col-md-6 mb-0'),
    #             Column('date', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Row(
    #             Column('cutside1', css_class='form-group col-md-4 mb-0'),
    #             Column('cutside2', css_class='form-group col-md-4 mb-0'),
    #             Column('cutside3', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Submit('submit', 'Submit', css_class='btn btn-primary')
    #     )

        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].initial = datetime.date.today()  # Set initial value to today's date

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        # fields = '__all__'


