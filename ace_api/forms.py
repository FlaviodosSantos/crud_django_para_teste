from django import forms
from .models import  Indice


class IndiceForm(forms.ModelForm):

    class Meta:
        model = Indice
        fields = '__all__'