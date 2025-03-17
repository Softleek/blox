from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PersonalDataDeletionRequest(BaseModel):
    email = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_STATUS = [
        ("Pending Verification", "Pending Verification"),
        ("Pending Approval", "Pending Approval"),
        ("On Hold", "On Hold"),
        ("Deleted", "Deleted"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Pending Verification', null=True, blank=True)
    anonymization_matrix = models.CharField(max_length=255, null=True, blank=True)
    deletion_steps = models.ManyToManyField("frappe_app.PersonalDataDeletionStep", related_name="PersonalDataDeletionRequestDeletionSteps", )
