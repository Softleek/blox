from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EnergyPointSettings(SingletonModel):
    enabled = models.BooleanField(default=False, null=True, blank=True)
    review_levels = models.ManyToManyField("frappe_app.ReviewLevel", related_name="EnergyPointSettingsReviewLevels", )
    CHOICES_POINT_ALLOCATION_PERIODICITY = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
    ]
    point_allocation_periodicity = models.CharField(choices=CHOICES_POINT_ALLOCATION_PERIODICITY, max_length=255, default='Weekly', null=True, blank=True)
    last_point_allocation_date = models.DateField(null=True, blank=True)
