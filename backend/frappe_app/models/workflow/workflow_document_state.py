from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkflowDocumentState(BaseModel):
    state = models.ForeignKey("frappe_app.WorkflowState", related_name="WorkflowDocumentStateState", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_DOC_STATUS = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
    ]
    doc_status = models.CharField(choices=CHOICES_DOC_STATUS, max_length=255, default='0', null=True, blank=True)
    CHOICES_UPDATE_FIELD = [
        ("", ""),
    ]
    update_field = models.CharField(choices=CHOICES_UPDATE_FIELD, max_length=255, null=True, blank=True)
    update_value = models.CharField(max_length=255, null=True, blank=True)
    allow_edit = models.ForeignKey("frappe_app.Role", related_name="WorkflowDocumentStateAllowEdit", on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    next_action_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="WorkflowDocumentStateNextActionEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    is_optional_state = models.BooleanField(default=False, null=True, blank=True)
    workflow_builder_id = models.CharField(max_length=255, null=True, blank=True)
    avoid_status_override = models.BooleanField(default=False, null=True, blank=True)
