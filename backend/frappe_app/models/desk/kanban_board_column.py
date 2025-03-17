from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class KanbanBoardColumn(BaseModel):
    column_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Active", "Active"),
        ("Archived", "Archived"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Active', null=True, blank=True)
    CHOICES_INDICATOR = [
        ("Blue", "Blue"),
        ("Cyan", "Cyan"),
        ("Gray", "Gray"),
        ("Green", "Green"),
        ("Light Blue", "Light Blue"),
        ("Orange", "Orange"),
        ("Pink", "Pink"),
        ("Purple", "Purple"),
        ("Red", "Red"),
        ("Yellow", "Yellow"),
    ]
    indicator = models.CharField(choices=CHOICES_INDICATOR, max_length=255, default='Gray', null=True, blank=True)
    order = models.CharField(max_length=255, null=True, blank=True)
