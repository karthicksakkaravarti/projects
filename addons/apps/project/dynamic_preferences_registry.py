from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

from config.helpers.dynamic_preferences_type_registry import JSONPreference

section = Section("app_project")


@global_preferences_registry.register
class ProjectForm(JSONPreference):

    section = section
    name = 'project_form'
    default = {
        'fields': [
            {
                "name": "Project Name",
                "fieldtype": "TextField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "name",
                "required": True,
                "readonly": False,
            },
            {
                "name": "Description",
                "fieldtype": "WYSIWYG",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "description",
                "required": True,
                "readonly": False,
            },
            {
                "name": "Start Date",
                "fieldtype": "DateField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "start_date",
                "required": True,
                "readonly": False,
            },
            {
                "name": "End Date",
                "fieldtype": "DateField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "end_date",
                "required": True,
                "readonly": False,
            },
            {
                "name": "Domain",
                "fieldtype": "TextField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "domain",
                "required": False,
                "readonly": False,
            }
        ]
    }
    required = False
