import django_filters as filter
from django.db.models import Q
import json
from config.helpers.Exception import exception
import datetime


class BaseFilter(filter.FilterSet):
    include_query = filter.CharFilter(method='generate_include_query_filter')
    exclude_query = filter.CharFilter(method='generate_exclude_query_filter')

    def generate_include_query_filter(self, queryset, value, *args, **kwargs):
        date_condition = ['range', 'gt', 'lt', 'lte', 'gte']
        try:
            if args:
                argument_dict = json.loads(args[0])
                and_condition = Q()
                for key, value in argument_dict.items():
                    find_condition = key.split('__')
                    if find_condition[1] in date_condition:
                        new_value = datetime.datetime.strptime(value, '%Y-%m-%d')
                        if find_condition[1] == 'range':
                            and_condition.add(Q(**{key: [new_value, new_value]}), Q.AND)
                        else:
                            and_condition.add(Q(**{key: new_value}), Q.AND)
                    else:
                        and_condition.add(Q(**{key: value}), Q.AND)

                return queryset.filter(and_condition)
        except Exception as e:
            exception(e)
        return queryset

    def generate_exclude_query_filter(self, queryset, value, *args, **kwargs):
        date_condition = ['range', 'gt', 'lt', 'lte', 'gte']
        try:
            if args:
                argument_dict = json.loads(args[0])
                and_condition = Q()
                for key, value in argument_dict.items():
                    find_condition = key.split('__')
                    if find_condition[1] in date_condition:
                        new_value = datetime.datetime.strptime(value, '%Y-%m-%d')
                        if find_condition[1] == 'range':
                            and_condition.add(Q(**{key: [new_value, new_value]}), Q.AND)
                        else:
                            and_condition.add(Q(**{key: new_value}), Q.AND)
                    else:
                        and_condition.add(Q(**{key: value}), Q.AND)

                return queryset.exclude(and_condition)
        except Exception as e:
            exception(e)
        return queryset
