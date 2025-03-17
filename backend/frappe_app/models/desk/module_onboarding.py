from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ModuleOnboarding(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="ModuleOnboardingModule", on_delete=models.CASCADE, null=True, blank=True)
    success_message = models.CharField(max_length=255, null=True, blank=True)
    documentation_url = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    steps = models.ManyToManyField("frappe_app.OnboardingStepMap", related_name="ModuleOnboardingSteps", )
    allow_roles = models.ManyToManyField("frappe_app.OnboardingPermission", related_name="ModuleOnboardingAllowRoles", )
