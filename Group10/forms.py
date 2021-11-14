from django import forms

class data(forms.Form):
    Emissions = forms.FloatField( required=True, max_value=16.0, min_value=0.0,error_messages={'required': 'Please enter this field','max_value':'16.0', 'min_value':'0.0'})
    Absorptions = forms.FloatField( required=True, max_value=16.0, min_value=0.0,error_messages={'required': 'Please enter this field','max_value':'16.0', 'min_value':'0.0'})
