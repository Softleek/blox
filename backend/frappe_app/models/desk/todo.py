from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class ToDo(BaseModel):
    CHOICES_STATUS = [
        ("Open", "Open"),
        ("Closed", "Closed"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Open', null=True, blank=True)
    CHOICES_PRIORITY = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]
    priority = models.CharField(choices=CHOICES_PRIORITY, max_length=255, default='Medium', null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(default='Today', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    reference_type = models.ForeignKey("frappe_app.Doctype", related_name="ToDoReferenceType", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey("frappe_app.Role", related_name="ToDoRole", on_delete=models.CASCADE, null=True, blank=True)
    assigned_by = models.ForeignKey("frappe_app.User", related_name="ToDoAssignedBy", on_delete=models.CASCADE, null=True, blank=True)
    assigned_by_full_name = models.CharField(max_length=255, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    assignment_rule = models.ForeignKey("frappe_app.AssignmentRule", related_name="ToDoAssignmentRule", on_delete=models.CASCADE, null=True, blank=True)
    allocated_to = models.ForeignKey("frappe_app.User", related_name="ToDoAllocatedTo", on_delete=models.CASCADE, null=True, blank=True)
