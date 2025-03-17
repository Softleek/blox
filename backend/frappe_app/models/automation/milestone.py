from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Milestone(BaseModel):
    reference_type = models.ForeignKey("frappe_app.Doctype", related_name="MilestoneReferenceType", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    track_field = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    milestone_tracker = models.ForeignKey("frappe_app.MilestoneTracker", related_name="MilestoneMilestoneTracker", on_delete=models.CASCADE, null=True, blank=True)
