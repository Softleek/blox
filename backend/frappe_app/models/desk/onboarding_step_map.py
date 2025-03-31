from django.db import models
from multiselectfield import MultiSelectField
import uuid
import os
from django.conf import settings
from core.models.template import BaseModel

class OnboardingStepMap(BaseModel):
    step = models.ForeignKey("frappe_app.OnboardingStep", related_name="OnboardingStepMapStep", on_delete=models.CASCADE, null=True, blank=True)
