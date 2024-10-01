import json

import dynamic_preferences
from django.core.validators import URLValidator
from django import forms
from django.forms import JSONField
from dynamic_preferences.serializers import BaseSerializer
from dynamic_preferences.types import StringPreference


class URLPreference(StringPreference):
    field_class = forms.URLField

    def validate(self, value):
        super().validate(value)
        URLValidator()(value)


class JSONPreferenceSerializer(dynamic_preferences.types.BaseSerializer):

    @classmethod
    def clean_to_db_value(cls, value):
        return json.dumps(value)

    @classmethod
    def to_python(cls, value, **kwargs):
        try:
            return json.loads(value)
        except:
            raise cls.exception("Cannot deserialize value {0} to json".format(value))


class JSONPreference(dynamic_preferences.types.LongStringPreference):
    field_class = JSONField
    serializer = JSONPreferenceSerializer


