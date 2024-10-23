from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.types import StringPreference

from config.helpers.dynamic_preferences_type_registry import JSONPreference

section = Section("app_repositories")


@global_preferences_registry.register
class RepositoriesForm(JSONPreference):

    section = section
    name = 'repo_form'
    default = {
        'fields': [
            {
                "name": "Repo Name",
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
