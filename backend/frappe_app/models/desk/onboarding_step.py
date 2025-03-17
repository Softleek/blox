from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class OnboardingStep(BaseModel):
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ACTION = [
        ("Create Entry", "Create Entry"),
        ("Update Settings", "Update Settings"),
        ("Show Form Tour", "Show Form Tour"),
        ("View Report", "View Report"),
        ("Go to Page", "Go to Page"),
        ("Watch Video", "Watch Video"),
    ]
    action = models.CharField(choices=CHOICES_ACTION, max_length=255, null=True, blank=True)
    reference_document = models.ForeignKey("frappe_app.Doctype", related_name="OnboardingStepReferenceDocument", on_delete=models.CASCADE, null=True, blank=True)
    reference_report = models.ForeignKey("frappe_app.Report", related_name="OnboardingStepReferenceReport", on_delete=models.CASCADE, null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    report_type = models.CharField(max_length=255, null=True, blank=True)
    is_skipped = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_FIELD = [
        ("", ""),
    ]
    field = models.CharField(choices=CHOICES_FIELD, max_length=255, null=True, blank=True)
    value_to_validate = models.CharField(max_length=255, null=True, blank=True)
    report_description = models.CharField(max_length=255, null=True, blank=True)
    report_reference_doctype = models.CharField(max_length=255, null=True, blank=True)
    is_single = models.BooleanField(default=False, null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    callback_title = models.CharField(max_length=255, null=True, blank=True)
    callback_message = models.TextField(null=True, blank=True)
    validate_action = models.BooleanField(default=True, null=True, blank=True)
    show_full_form = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    intro_video_url = models.CharField(max_length=255, null=True, blank=True)
    action_label = models.CharField(max_length=255, null=True, blank=True)
    show_form_tour = models.BooleanField(default=False, null=True, blank=True)
    form_tour = models.ForeignKey("frappe_app.FormTour", related_name="OnboardingStepFormTour", on_delete=models.CASCADE, null=True, blank=True)
