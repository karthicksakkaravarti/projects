from django import forms
from django.contrib import admin
from .models import Project, Attribute

# Register your models here.

class DynamicFieldForm(forms.ModelForm):
    new_field_name = forms.CharField(required=False, label="New Field Name")
    new_field_type = forms.ChoiceField(choices=Attribute.DATA_TYPES, required=False, label="New Field Type")
    new_field_value = forms.CharField(widget=forms.Textarea, required=False, label="New Field Value")

    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            for field_name, field_value in self.instance.additional_fields.items():
                self.fields[f'dynamic_{field_name}'] = forms.CharField(
                    initial=field_value,
                    required=False,
                    label=f"Dynamic Field: {field_name}"
                )

    def clean(self):
        cleaned_data = super().clean()
        new_field_name = cleaned_data.get('new_field_name')
        new_field_type = cleaned_data.get('new_field_type')
        new_field_value = cleaned_data.get('new_field_value')

        if new_field_name and not new_field_type:
            raise forms.ValidationError("Field type is required when adding a new field.")
        if new_field_type and not new_field_name:
            raise forms.ValidationError("Field name is required when adding a new field.")

        return cleaned_data

class ProjectAdmin(admin.ModelAdmin):
    form = DynamicFieldForm
    list_display = ('name', 'owner', 'start_date', 'end_date')

    def save_model(self, request, obj, form, change):
        # Handle existing dynamic fields
        for field_name, field_value in form.cleaned_data.items():
            if field_name.startswith('dynamic_'):
                real_field_name = field_name[8:]  # Remove 'dynamic_' prefix
                obj.additional_fields[real_field_name] = field_value

        # Handle new dynamic field
        new_field_name = form.cleaned_data.get('new_field_name')
        new_field_type = form.cleaned_data.get('new_field_type')
        new_field_value = form.cleaned_data.get('new_field_value')

        if new_field_name and new_field_type:
            # Convert the value to the appropriate type
            if new_field_type == 'int':
                new_field_value = int(new_field_value)
            elif new_field_type == 'float':
                new_field_value = float(new_field_value)
            elif new_field_type == 'bool':
                new_field_value = new_field_value.lower() in ['true', 'yes', '1']
            
            obj.additional_fields[new_field_name] = new_field_value

        super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            dynamic_fields = [(f'dynamic_{name}', name) for name in obj.additional_fields.keys()]
            fieldsets += (
                ('Dynamic Fields', {
                    'fields': dynamic_fields + [
                        ('new_field_name', 'new_field_type', 'new_field_value')
                    ]
                }),
            )
        return fieldsets

admin.site.register(Project, ProjectAdmin)

# create intergface to add attributes to the description field