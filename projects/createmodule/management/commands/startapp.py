import json
import os

from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
import re
from config.settings.base import ADDONS_APPS
class Command(TemplateCommand):
    help = "Custom startapp command."
    type = 'app'

    def handle(self, *args, **options):
        app_name = options.get('name')

        if not app_name:
            raise CommandError("You must provide an application name.")

        if not re.match('^[a-z0-9_]+$', app_name):
            raise CommandError("Invalid application name. Use only lowercase letters, numbers, and underscores.")

        if ' ' in app_name:
            raise CommandError("Spaces are not allowed in the application name.")

        absolute_target_directory = os.path.abspath(os.path.join(ADDONS_APPS, app_name))

        # Create the directory if it doesn't exist
        os.makedirs(absolute_target_directory, exist_ok=True)

        # Ask user for additional info
        info = {
            "name": input("Module name: "),
            "author": input("Author's name: "),
            "description": input("A description: "),
            "category": input("Category: Sales, Productive, Production etc... : "),
            "version": input("Please enter a version: (v 1.0.1): "),
        }
        options['info'] = info
        if options['template'] is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            template_path = os.path.join(current_dir, '../../erp_template')
            options['template'] = template_path


        # Call the super class' `handle` method to create the app
        super().handle('app', *args,target=absolute_target_directory, **options)

        # Write the `info.py-tpl` file
        # target = os.path.join(options['directory'], app_name)
        # info_file_path = os.path.join(target, 'info.py-tpl')
        #
        # with open(info_file_path, 'w') as f:
        #     json.dump(info, f, indent=4)
