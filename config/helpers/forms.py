import json
from rest_framework import serializers


class ValueList(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)
    value = serializers.CharField(allow_blank=True)


class ValueField(serializers.Field):

    def get_attribute(self, instance):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.
        return instance
     
    def to_representation(self, value):
        try:
            print(self.context.get('request', {}))
            for query, query_value in self.context.get('request', {}).items():
                print(value.get('dbfield'), query)
                if value.get('dbfield') == query:
                    try:
                        if value.get('itemvalue') == 'id':
                            return int(query_value)
                    except Exception as e:
                        return query_value
                    return query_value
            else:
                return value['value']
        except Exception as e:
            print(e)
            return value['value']
    def to_internal_value(self, data):
        return data

class LayoutSeralizers(serializers.Serializer):
    name = serializers.CharField(allow_blank=True)
    fieldtype = serializers.CharField()
    sm = serializers.CharField()
    valuelist = ValueList(many=True)
    value = ValueField()
    dbfield = serializers.CharField(allow_blank=True)
    customtable = serializers.BooleanField(required=False)
    customfieldname = serializers.CharField(required=False)
    required = serializers.BooleanField(required=False)
    max_length = serializers.IntegerField(required=False)
    other_rules = serializers.ListField(required=False)
    itemtext = serializers.CharField(required=False)
    itemvalue = serializers.CharField(required=False)
    prependicon = serializers.CharField(required=False)
    maxdate_field = serializers.CharField(required=False)
    mindate_field = serializers.CharField(required=False)
    menu = serializers.BooleanField(required=False)
    clearable = serializers.BooleanField(required=False)
    conditioncheck = serializers.BooleanField(required=False)
    conditionfield = serializers.CharField(required=False)
    conditionfield1 = serializers.CharField(required=False)
    conditionvalue = serializers.CharField(required=False)
    conditionvalue1 = serializers.CharField(required=False)
    conditionlabel = serializers.CharField(required=False)
    type = serializers.CharField(required=False)
    rows = serializers.IntegerField(required=False)
    prefix = serializers.CharField(required=False)
    appendicon = serializers.CharField(required=False)
    readonly = serializers.SerializerMethodField(required=False)
    prependinnericon = serializers.CharField(required=False)
    rowheight = serializers.IntegerField(required=False)
    error_message = serializers.CharField(required=False, default=None)
    outlined = serializers.BooleanField(required=False)
    dbtable = serializers.CharField(required=False)
    hint = serializers.CharField(required=False)
    multiple = serializers.BooleanField(required=False)
    mindate = serializers.CharField(required=False)
    maxdate = serializers.CharField(required=False)
    style = serializers.CharField(required=False)
    yesicon = serializers.CharField(required=False)
    yestooltip = serializers.CharField(required=False)
    noicon = serializers.CharField(required=False)
    notooltip = serializers.CharField(required=False)
    inline = serializers.BooleanField(required=False)
    hideselected = serializers.BooleanField(required=False)

    def get_readonly(self, obj):
        return False


class FormsSerializers(serializers.Serializer):
    layout = LayoutSeralizers(many=True)
