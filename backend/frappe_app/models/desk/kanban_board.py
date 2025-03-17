from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class KanbanBoard(BaseModel):
    kanban_board_name = models.CharField(max_length=255, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="KanbanBoardReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_FIELD_NAME = [
        ("", ""),
    ]
    field_name = models.CharField(choices=CHOICES_FIELD_NAME, max_length=255, null=True, blank=True)
    columns = models.ManyToManyField("frappe_app.KanbanBoardColumn", related_name="KanbanBoardColumns", )
    filters = models.CharField(max_length=255, null=True, blank=True)
    private = models.BooleanField(default=False, null=True, blank=True)
    fields = models.CharField(max_length=255, null=True, blank=True)
    show_labels = models.BooleanField(default=False, null=True, blank=True)
