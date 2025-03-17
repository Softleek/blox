from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkflowAction(BaseModel):
    CHOICES_STATUS = [
        ("Open", "Open"),
        ("Completed", "Completed"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="WorkflowActionReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("frappe_app.User", related_name="WorkflowActionUser", on_delete=models.CASCADE, null=True, blank=True)
    workflow_state = models.CharField(max_length=255, null=True, blank=True)
    completed_by = models.ForeignKey("frappe_app.User", related_name="WorkflowActionCompletedBy", on_delete=models.CASCADE, null=True, blank=True)
    completed_by_role = models.ForeignKey("frappe_app.Role", related_name="WorkflowActionCompletedByRole", on_delete=models.CASCADE, null=True, blank=True)
    permitted_roles = models.ManyToManyField("frappe_app.WorkflowActionPermittedRole", related_name="WorkflowActionPermittedRoles", )
