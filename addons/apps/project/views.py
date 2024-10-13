from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

    
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from .forms import DynamicFieldForm

def add_dynamic_field(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        form = DynamicFieldForm(request.POST)
        if form.is_valid():
            field_name = form.cleaned_data['field_name']
            field_type = form.cleaned_data['field_type']
            field_value = form.cleaned_data['field_value']
            
            # Convert the value to the appropriate type
            if field_type == 'int':
                field_value = int(field_value)
            elif field_type == 'float':
                field_value = float(field_value)
            elif field_type == 'bool':
                field_value = field_value.lower() in ['true', 'yes', '1']
            
            # Add the new field to the project's additional_fields
            print(field_name, field_type, field_value)
            project.set_attribute(field_name, field_value, field_type)
            project.save()
            
            messages.success(request, f"Field '{field_name}' added successfully.")
            return HttpResponse("Field added successfully")
    else:
        form = DynamicFieldForm()
    
    return render(request, 'project/add_dynamic_field.html', {'form': form, 'project': project})