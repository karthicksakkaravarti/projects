from dynamic_preferences.types import BooleanPreference, StringPreference, FilePreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry

setup = Section('setup')

@global_preferences_registry.register
class AppName(StringPreference):
    section = setup
    name = 'app_name'
    default = 'MyApp'
    verbose_name = 'App Name'

@global_preferences_registry.register
class AppLogo(FilePreference):
    section = setup
    name = 'app_logo'
    verbose_name = 'App Logo'

@global_preferences_registry.register
class AppFavicon(FilePreference):
    section = setup
    name = 'app_favicon'
    verbose_name = 'App Favicon'

@global_preferences_registry.register
class IsSetupComplete(BooleanPreference):
    section = setup
    name = 'is_setup_complete'
    default = False
    verbose_name = 'Is setup complete?'
