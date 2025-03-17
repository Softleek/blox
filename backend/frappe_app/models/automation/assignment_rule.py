from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AssignmentRule(BaseModel):
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="AssignmentRuleDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField(default='Automatic Assignment', null=True, blank=True)
    assign_condition = models.CharField(max_length=255, null=True, blank=True)
    unassign_condition = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_RULE = [
        ("Round Robin", "Round Robin"),
        ("Load Balancing", "Load Balancing"),
        ("Based on Field", "Based on Field"),
    ]
    rule = models.CharField(choices=CHOICES_RULE, max_length=255, null=True, blank=True)
    users = models.ManyToManyField("frappe_app.AssignmentRuleUser", related_name="AssignmentRuleUsers", )
    last_user = models.ForeignKey("frappe_app.User", related_name="AssignmentRuleLastUser", on_delete=models.CASCADE, null=True, blank=True)
    close_condition = models.CharField(max_length=255, null=True, blank=True)
    assignment_days = models.ManyToManyField("frappe_app.AssignmentRuleDay", related_name="AssignmentRuleAssignmentDays", )
    CHOICES_DUE_DATE_BASED_ON = [
        ("", ""),
    ]
    due_date_based_on = models.CharField(choices=CHOICES_DUE_DATE_BASED_ON, max_length=255, null=True, blank=True)
    CHOICES_FIELD = [
        ("", ""),
    ]
    field = models.CharField(choices=CHOICES_FIELD, max_length=255, null=True, blank=True)
