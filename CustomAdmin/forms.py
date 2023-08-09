from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from BakersApp.models import Cakes, TutorialVideo

class AddCakeForm(forms.ModelForm):
    class Meta:
        model = Cakes
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(AddCakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class AddTutorialForm(forms.ModelForm):
    class Meta:
        model = TutorialVideo
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(AddTutorialForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'   
    
