from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OnboardingStepMap(BaseModel):
    step = models.ForeignKey("frappe_app.OnboardingStep", related_name="OnboardingStepMapStep", on_delete=models.CASCADE, null=True, blank=True)
