from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Workspace(BaseModel):
    label = models.CharField(max_length=255, null=True, blank=True)
    charts = models.ManyToManyField("frappe_app.WorkspaceChart", related_name="WorkspaceCharts", )
    shortcuts = models.ManyToManyField("frappe_app.WorkspaceShortcut", related_name="WorkspaceShortcuts", )
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="WorkspaceRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="WorkspaceModule", on_delete=models.CASCADE, null=True, blank=True)
    for_user = models.CharField(max_length=255, null=True, blank=True)
    hide_custom = models.BooleanField(default=False, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    links = models.ManyToManyField("frappe_app.WorkspaceLink", related_name="WorkspaceLinks", )
    public = models.BooleanField(default=False, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    parent_page = models.ForeignKey("frappe_app.Workspace", related_name="WorkspaceParentPage", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(default='[]', null=True, blank=True)
    sequence_id = models.FloatField(null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="WorkspaceRoles", )
    quick_lists = models.ManyToManyField("frappe_app.WorkspaceQuickList", related_name="WorkspaceQuickLists", )
    is_hidden = models.BooleanField(default=False, null=True, blank=True)
    number_cards = models.ManyToManyField("frappe_app.WorkspaceNumberCard", related_name="WorkspaceNumberCards", )
    custom_blocks = models.ManyToManyField("frappe_app.WorkspaceCustomBlock", related_name="WorkspaceCustomBlocks", )
    CHOICES_INDICATOR_COLOR = [
        ("green", "green"),
        ("cyan", "cyan"),
        ("blue", "blue"),
        ("orange", "orange"),
        ("yellow", "yellow"),
        ("gray", "gray"),
        ("grey", "grey"),
        ("red", "red"),
        ("pink", "pink"),
        ("darkgrey", "darkgrey"),
        ("purple", "purple"),
        ("light-blue", "light-blue"),
    ]
    indicator_color = models.CharField(choices=CHOICES_INDICATOR_COLOR, max_length=255, null=True, blank=True)
    app = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_TYPE = [
        ("Workspace", "Workspace"),
        ("Link", "Link"),
        ("URL", "URL"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, default='Workspace', null=True, blank=True)
    CHOICES_LINK_TYPE = [
        ("DocType", "DocType"),
        ("Page", "Page"),
        ("Report", "Report"),
    ]
    link_type = models.CharField(choices=CHOICES_LINK_TYPE, max_length=255, null=True, blank=True)
    link_to = models.CharField(max_length=255, null=True, blank=True)
    external_link = models.CharField(max_length=255, null=True, blank=True)
