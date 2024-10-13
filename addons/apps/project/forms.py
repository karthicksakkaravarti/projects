from django import forms
from .models import Project, Attribute

class DynamicFieldForm(forms.Form):
    field_name = forms.CharField(max_length=255, label="Field Name")
    field_type = forms.ChoiceField(choices=Attribute.DATA_TYPES, label="Field Type")
    field_value = forms.CharField(widget=forms.Textarea, label="Field Value")

    def clean_field_name(self):
        field_name = self.cleaned_data['field_name']
        if ' ' in field_name:
            raise forms.ValidationError("Field name cannot contain spaces.")
        return field_name