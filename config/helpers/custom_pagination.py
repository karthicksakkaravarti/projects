from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(LimitOffsetPagination):
    default_limit = 10  # Set your default page size here
    max_limit = 100  # Set the maximum allowed page size here
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    page_query_param = 'page'

    def paginate_queryset(self, queryset, request, view=None):
        if self.page_query_param in request.query_params:
            self.default_paginator = PageNumberPagination()
            return self.default_paginator.paginate_queryset(queryset, request, view)
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if hasattr(self, 'default_paginator') and hasattr(self.default_paginator, 'page'):
            return self.default_paginator.get_paginated_response(data)
        return Response({
            'total_pages': self.get_total_pages(),
            'total_count': self.count,  # Here is your total count
            'results': data,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
        })

    def get_total_pages(self):
        if self.limit is None:
            return None
        total_pages = divmod(self.count, self.limit)[0]
        if self.count % self.limit > 0:
            total_pages += 1
        return total_pages
