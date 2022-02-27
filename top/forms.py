from django import forms
from.models import Ingredient

class FindForm(forms.Form):
    find = forms.CharField(label='find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))