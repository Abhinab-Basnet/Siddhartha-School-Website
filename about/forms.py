from django import forms
from .models import EntranceApplication

class EntranceApplicationForm(forms.ModelForm):
    class Meta:
        model = EntranceApplication
        fields = '__all__' # This includes all fields from the model
        widgets = {
            'dob_ad': forms.DateInput(attrs={'type': 'date'}),
        }