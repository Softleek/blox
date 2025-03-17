from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CalendarView(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="CalendarViewReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_SUBJECT_FIELD = [
        ("", ""),
    ]
    subject_field = models.CharField(choices=CHOICES_SUBJECT_FIELD, max_length=255, null=True, blank=True)
    CHOICES_START_DATE_FIELD = [
        ("", ""),
    ]
    start_date_field = models.CharField(choices=CHOICES_START_DATE_FIELD, max_length=255, null=True, blank=True)
    CHOICES_END_DATE_FIELD = [
        ("", ""),
    ]
    end_date_field = models.CharField(choices=CHOICES_END_DATE_FIELD, max_length=255, null=True, blank=True)
    all_day = models.BooleanField(default=False, null=True, blank=True)
