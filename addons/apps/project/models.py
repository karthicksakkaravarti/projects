from django.db import models
from django.core.exceptions import ValidationError
from django_fsm import FSMIntegerField, transition
import uuid

class WYSIWYGTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.field_type = kwargs.pop('field_type', 'WYSIWYG')
        super().__init__(*args, **kwargs)


class Attribute(models.Model):
    DATA_TYPES = [
        ('char', 'Text'),
        ('int', 'Integer'),
        ('bool', 'Boolean'),
        ('date', 'Date'),
        ('float', 'Float'),
    ]
    name = models.CharField(max_length=255, unique=True)
    data_type = models.CharField(max_length=10, choices=DATA_TYPES)

    def __str__(self):
        return self.name


class ProjectAttributeValue(models.Model):
    project = models.ForeignKey(
        "Project", related_name='attribute_values', on_delete=models.CASCADE)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    value_char = models.CharField(max_length=255, blank=True, null=True)
    value_int = models.IntegerField(blank=True, null=True)
    value_bool = models.BooleanField(blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)

    # def clean(self):
    #     if self.attribute.data_type == 'char' and not self.value_char:
    #         raise ValidationError('This attribute requires a text value.')
    #     elif self.attribute.data_type == 'int' and self.value_int is None:
    #         raise ValidationError('This attribute requires an integer value.')
    #     elif self.attribute.data_type == 'bool' and self.value_bool is None:
    #         raise ValidationError('This attribute requires a boolean value.')
    #     elif self.attribute.data_type == 'date' and not self.value_date:
    #         raise ValidationError('This attribute requires a date value.')
    #     elif self.attribute.data_type == 'float' and self.value_float is None:
    #         raise ValidationError('This attribute requires a float value.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_value(self):
        return getattr(self, f'value_{self.attribute.data_type}')


class Project(models.Model):
    DRAFT = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    ON_HOLD = 4
    CANCELLED = 5
    REJECTED = 6
    STATUS = [
        (DRAFT, 'Draft'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (ON_HOLD, 'On Hold'),
        (CANCELLED, 'Cancelled'),
        (REJECTED, 'Rejected'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='Project Name')
    description = WYSIWYGTextField(verbose_name='Description', field_type='WYSIWYG')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    status = FSMIntegerField(choices=STATUS, default=DRAFT, verbose_name="Status")
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Owner')

    @classmethod
    def get_description_field(cls):
        return cls._meta.get_field('description')
        

    def set_attribute(self, attr_name, value, data_type):
        print(attr_name, value)
        attribute, created = Attribute.objects.get_or_create(name=attr_name, data_type=data_type)
        print(attribute)
        pav, created = ProjectAttributeValue.objects.get_or_create(
            project=self, attribute=attribute)
        if attribute.data_type == 'char':
            print("setting char")
            pav.value_char = value
        elif attribute.data_type == 'int':
            pav.value_int = value
        elif attribute.data_type == 'bool':
            pav.value_bool = value
        elif attribute.data_type == 'date':
            pav.value_date = value
        elif attribute.data_type == 'float':
            pav.value_float = value
        pav.save()

    def get_attribute(self, attr_name):
        try:
            attribute = Attribute.objects.get(name=attr_name)
            pav = ProjectAttributeValue.objects.get(
                project=self, attribute=attribute)
            return pav.get_value()
        except (Attribute.DoesNotExist, ProjectAttributeValue.DoesNotExist):
            return None

    def __str__(self):
        return self.name