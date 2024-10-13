import os
import subprocess
import re
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Validates the given app using flake8, unit tests, and coverage'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the app to validate')
        parser.add_argument('--test-settings', type=str, default='core.config.settings.test', 
                            help='The settings file to use when running tests')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        settings_module = kwargs['test_settings']
        app_abs_path = os.path.abspath(f'./addons/apps/{app_name}')
        self._run_flake8(app_name, app_abs_path)
        self._run_coverage(app_name, app_abs_path, settings_module)

    def _run_flake8(self, app_name, app_path):
        result = subprocess.run(['flake8', app_path], capture_output=True, text=True)
        self.stdout.write(self.style.SUCCESS(f'Static Code Analysis {app_name}...'))
        if result.returncode != 0:
            errors = result.stdout.splitlines()
            self.stdout.write(self.style.ERROR(f'flake8 found {len(errors)} issues in {app_name}:'))
            self.stdout.write('+----------------------------------+------+-------+----------------------------------------------+')
            self.stdout.write('| File                             | Line | Col   | Message                                      |')
            self.stdout.write('+----------------------------------+------+-------+----------------------------------------------+')
            for error in errors:
                file_path, location, message = error.split(':', 2)
                relative_path = file_path.split('addons', 1)[-1]  # will give "/app/file_name"
                location_parts = location.split(',')
                line = location_parts[0]
                col = location_parts[1] if len(location_parts) > 1 else ''
                self.stdout.write(f'| addons{relative_path:32} | {line:4} | {col:5} | {message:44} |')
            self.stdout.write('+----------------------------------+------+-------+----------------------------------------------+')
        else:
            self.stdout.write(self.style.SUCCESS(f'flake8 passed for {app_name}!'))

    def _run_coverage(self, app_name, app_path, settings_module):
        # Run tests and capture output
        test_cmd = ['python', 'manage.py', 'test', f'addons.apps.{app_name}.tests', f'--settings={settings_module}', '--verbosity=2']
        test_coverage_cmd = ['manage.py', 'test', f'addons.apps.{app_name}.tests', f'--settings={settings_module}', '--verbosity=2']
        test_result = subprocess.run(test_cmd, capture_output=True, text=True)
        test_results = self.parse_test_output(test_result.stdout + test_result.stderr)
        if self.print_test_report(test_results):
            # Run coverage
            coverage_cmd = ['coverage', 'run', f'--source={app_path}'] + test_coverage_cmd
            subprocess.run(coverage_cmd)
            # Display coverage report
            report_result = subprocess.run(['coverage', 'report', '-m'], capture_output=True, text=True)
            self.stdout.write(self.style.SUCCESS('-----------------------------Code Coverage Report-----------------------------'))
            for line in report_result.stdout.splitlines():
                self.stdout.write(line)
        else:
            self.stdout.write(self.style.ERROR('No Test cases Found'))

    def parse_test_output(self, output):
        pattern = re.compile(r"^(?P<status>FAIL|ERROR|OK): (?P<test_case>\w+) \((?P<module_path>[\w\.]+)\)$")
        lines = output.splitlines()
        test_results = [match.groupdict() for line in lines for match in [pattern.search(line)] if match]
        return test_results

    def print_test_report(self, test_results):
        self.stdout.write(self.style.SUCCESS('-----------------------------Unit Test case Report-----------------------------'))
        if not test_results:
            return False
        header = "+-----------------------+------------------------------------------+--------+"
        self.stdout.write(header)
        self.stdout.write("| Test Case Name        | Module Path                              | Status |")
        self.stdout.write(header)

        for result in test_results:
            self.stdout.write(f"| {result['test_case']:<21} | {result['module_path']:<40} | {result['status']:<6} |")
            self.stdout.write(header)
        return True    