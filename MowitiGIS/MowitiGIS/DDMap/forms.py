from django import forms
from .models import Punct_de_interes


class addPoi(forms.ModelForm):
    class Meta:
        model = Punct_de_interes
        fields = ['location', 'poi_type']
