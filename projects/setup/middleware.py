from django.http import HttpResponseRedirect
from dynamic_preferences.registries import global_preferences_registry


class SetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        global_preferences = global_preferences_registry.manager()
        is_setup_complete = global_preferences['setup__is_setup_complete']
        if not is_setup_complete:
            if request.path != '/setup/':
                return HttpResponseRedirect('/setup/')
