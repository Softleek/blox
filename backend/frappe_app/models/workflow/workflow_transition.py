from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkflowTransition(BaseModel):
    state = models.ForeignKey("frappe_app.WorkflowState", related_name="WorkflowTransitionState", on_delete=models.CASCADE, null=True, blank=True)
    action = models.ForeignKey("frappe_app.WorkflowActionMaster", related_name="WorkflowTransitionAction", on_delete=models.CASCADE, null=True, blank=True)
    next_state = models.ForeignKey("frappe_app.WorkflowState", related_name="WorkflowTransitionNextState", on_delete=models.CASCADE, null=True, blank=True)
    allowed = models.ForeignKey("frappe_app.Role", related_name="WorkflowTransitionAllowed", on_delete=models.CASCADE, null=True, blank=True)
    allow_self_approval = models.BooleanField(default=True, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)
    example = models.TextField(null=True, blank=True)
    workflow_builder_id = models.CharField(max_length=255, null=True, blank=True)
