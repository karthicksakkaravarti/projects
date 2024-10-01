import uuid
from django.db import models


class DropDownFieldValues(models.Model) :
    fieldname = models.CharField(max_length=50)
    fieldvalue = models.TextField()


class Criteria(models.Model):
    description = models.CharField(max_length=200)
    criteria = models.TextField()

    def __str__(self):
        return self.description


class CustomView(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    is_default = models.BooleanField()
