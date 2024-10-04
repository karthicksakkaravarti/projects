from config.helpers.Helpers import (
    generate_fields,
    generate_customview_list,
    generate_customview
)
from config.helpers.Exception import exception


class ColumnsMixin:
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        model = getattr(self, 'list_model', None)
        include_actions = getattr(self, 'include_actions', False)
        print("response", response.data)
        try:
            response.data['columns'] = generate_fields(
                'self', model, includeactions=include_actions)
            response.data['customview_list'] = generate_customview_list(1)
            response.data['customview'] = generate_customview(
                1, request.query_params.get('customview', None))
        except Exception as e:
            exception(e)  # Assuming you have an exception handler
        return response
