from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from BakersApp.models import Cakes

class AddCakeForm(forms.ModelForm):
    class Meta:
        model = Cakes
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(AddCakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditCakeForm(forms.Form):
    cName = forms.CharField(label="Cake Name", widget=forms.TextInput)
    cFlavour = forms.CharField(label="Cake Name", widget=forms.TextInput)
    