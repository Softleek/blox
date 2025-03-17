from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WorkspaceShortcut(BaseModel):
    CHOICES_TYPE = [
        ("DocType", "DocType"),
        ("Report", "Report"),
        ("Page", "Page"),
        ("Dashboard", "Dashboard"),
        ("URL", "URL"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, null=True, blank=True)
    link_to = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_DOC_VIEW = [
        ("List", "List"),
        ("Report Builder", "Report Builder"),
        ("Dashboard", "Dashboard"),
        ("Tree", "Tree"),
        ("New", "New"),
        ("Calendar", "Calendar"),
        ("Kanban", "Kanban"),
        ("Image", "Image"),
    ]
    doc_view = models.CharField(choices=CHOICES_DOC_VIEW, max_length=255, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="WorkspaceShortcutRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    stats_filter = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    format = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    kanban_board = models.ForeignKey("frappe_app.KanbanBoard", related_name="WorkspaceShortcutKanbanBoard", on_delete=models.CASCADE, null=True, blank=True)
