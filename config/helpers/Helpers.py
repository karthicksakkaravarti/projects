import json
import calendar
from _decimal import ROUND_DOWN, Decimal
import decimal
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
import coreapi
import coreschema
from datetime import datetime, timedelta, date
from django.db.models import F, Sum, ExpressionWrapper, fields
from django.db.models.fields import DurationField
from dynamic_preferences.registries import global_preferences_registry
from config.helpers.Exception import exception
from projects.setup import models as setupModel
from projects.setup.rest_api import serialierzer as setupserializers
form_name = coreapi.Field("form_name", location="query",
                          schema=coreschema.String(description="Form Name"))
fields = coreapi.Field("fields", location="query",
                       schema=coreschema.String(description="Fields to Return"))
global_preferences = global_preferences_registry.manager()


def generate_fields(view, model, includeactions=False, id_name="ID", preferences=None):
    try:
        defaultview = []
        ConfigView = []
        try:
            ConfigView = global_preferences[preferences].get(view)
        except Exception as e:
            exception(e)
            ConfigView = []

        # Looping fields
        for field in model._meta.fields:
            if ConfigView and field.name in ConfigView:
                if field.name in ['name', 'start_date', 'end_date']:
                    defaultview.append(
                        {"value": field.name, "text": field.verbose_name, "is_default": True})
                else:
                    defaultview.append(
                        {"value": field.name, "text": field.verbose_name, "is_default": True})

            elif view == 'self':
                if field.name == 'id':
                    defaultview.append(
                        {"value": field.name, "text": id_name, "is_default": True})
                else:
                    defaultview.append(
                        {"value": field.name, "text": field.verbose_name, "is_default": True})

            elif view == 'ResourceRequestView' and field.name in [
                'role', 'resource_number', 'allocation', 'start_date', 'end_date', 'resource_cost', 'team'
            ]:
                defaultview.append(
                    {"value": field.name, "text": field.verbose_name, "is_default": True})

            elif view == 'ProjectView' and field.verbose_name in USER_LINK_FIELDS:
                defaultview.append({"value": field.name, "text": field.verbose_name,
                                   "is_default": False, 'width': 250})
            else:
                defaultview.append(
                    {"value": field.name, "text": field.verbose_name, "is_default": False})
        if includeactions:
            defaultview.append(
                {"value": "actions", "text": "Actions", "is_default": True})

        return defaultview
    except Exception as e:
        exception(e)
        return []


def generate_customview_list(type):
    customview_list = setupserializers.CustomViewSerializers(
        setupModel.CustomView.objects.filter(type=type).order_by('sequence'), many=True)
    return customview_list.data


def generate_customview(type, id):
    if id:
        return setupserializers.CustomViewSerializers(setupModel.CustomView.objects.get(type=type, id=id)).data
    else:
        return setupserializers.CustomViewSerializers(setupModel.CustomView.objects.get(type=type, is_default=True)).data
