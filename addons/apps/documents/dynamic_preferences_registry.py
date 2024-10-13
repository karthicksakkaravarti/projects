from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

from config.helpers.dynamic_preferences_type_registry import JSONPreference

section = Section("app_documents")


@global_preferences_registry.register
class DocumentForm(JSONPreference):

    section = section
    name = 'document_form'
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
                "name": "Content",
                "fieldtype": "WYSIWYG",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "content",
                "required": True,
                "readonly": False,
            },
            {
                "name": "Category",
                "fieldtype": "TextField",
                "sm": "12",
                "valuelist": [],
                "value": "",
                "dbfield": "category",
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
