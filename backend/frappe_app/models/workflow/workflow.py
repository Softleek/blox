from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Workflow(BaseModel):
    workflow_name = models.CharField(max_length=255, null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="WorkflowDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    override_status = models.BooleanField(default=False, null=True, blank=True)
    send_email_alert = models.BooleanField(default=False, null=True, blank=True)
    states = models.ManyToManyField("frappe_app.WorkflowDocumentState", related_name="WorkflowStates", )
    transitions = models.ManyToManyField("frappe_app.WorkflowTransition", related_name="WorkflowTransitions", )
    workflow_state_field = models.CharField(max_length=255, default='workflow_state', null=True, blank=True)
    workflow_data = models.JSONField(null=True, blank=True)
