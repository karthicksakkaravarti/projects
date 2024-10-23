from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import BooleanPreference, IntegerPreference, StringPreference
from rest_framework.response import Response
from dynamic_preferences.types import StringPreference
from config.helpers.dynamic_preferences_type_registry import JSONPreference

section = Section('app_tasks')

@global_preferences_registry.register
class DefaultStatusPreference(StringPreference):
    section = section
    name = 'default_status'
    default = 'pending'
    help_text = 'Default status for new tasks'

@global_preferences_registry.register
class TaskForm(JSONPreference):

    section = section
    name = 'task_form'
    default = {
        "fields": [
            {
                "name": "Title",
                "fieldtype": "TextField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "title",
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
                "name": "Due Date",
                "fieldtype": "DateField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "due_date",
                "required": True,
                "readonly": False,
            },
            {
                "name": "Project",
                "fieldtype": "Hidden",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "project",
                "required": True,
                "readonly": False,
                "hidden": True,
            },

        ]
    }
    required = False
