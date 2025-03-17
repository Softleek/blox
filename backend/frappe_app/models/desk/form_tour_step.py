from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class FormTourStep(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    CHOICES_FIELDNAME = [
        ("", ""),
    ]
    fieldname = models.CharField(choices=CHOICES_FIELDNAME, max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_POSITION = [
        ("Left", "Left"),
        ("Left Center", "Left Center"),
        ("Left Bottom", "Left Bottom"),
        ("Top", "Top"),
        ("Top Center", "Top Center"),
        ("Top Right", "Top Right"),
        ("Right", "Right"),
        ("Right Center", "Right Center"),
        ("Right Bottom", "Right Bottom"),
        ("Bottom", "Bottom"),
        ("Bottom Center", "Bottom Center"),
        ("Bottom Right", "Bottom Right"),
        ("Mid Center", "Mid Center"),
    ]
    position = models.CharField(choices=CHOICES_POSITION, max_length=255, default='Bottom', null=True, blank=True)
    next_step_condition = models.CharField(max_length=255, null=True, blank=True)
    has_next_condition = models.BooleanField(default=False, null=True, blank=True)
    fieldtype = models.CharField(max_length=255, default='0', null=True, blank=True)
    is_table_field = models.BooleanField(default=False, null=True, blank=True)
    child_doctype = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_PARENT_FIELDNAME = [
        ("", ""),
    ]
    parent_fieldname = models.CharField(choices=CHOICES_PARENT_FIELDNAME, max_length=255, null=True, blank=True)
    ui_tour = models.BooleanField(default=False, null=True, blank=True)
    element_selector = models.CharField(max_length=255, null=True, blank=True)
    parent_element_selector = models.CharField(max_length=255, null=True, blank=True)
    next_form_tour = models.ForeignKey("frappe_app.FormTour", related_name="FormTourStepNextFormTour", on_delete=models.CASCADE, null=True, blank=True)
    hide_buttons = models.BooleanField(default=False, null=True, blank=True)
    next_on_click = models.BooleanField(default=False, null=True, blank=True)
    popover_element = models.BooleanField(default=False, null=True, blank=True)
    offset_x = models.IntegerField(default=0, null=True, blank=True)
    offset_y = models.IntegerField(default=0, null=True, blank=True)
    modal_trigger = models.BooleanField(default=False, null=True, blank=True)
    ondemand_description = models.TextField(null=True, blank=True)
