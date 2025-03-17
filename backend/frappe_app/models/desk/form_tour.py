from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class FormTour(BaseModel):
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="FormTourReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    steps = models.ManyToManyField("frappe_app.FormTourStep", related_name="FormTourSteps", )
    title = models.CharField(max_length=255, null=True, blank=True)
    save_on_complete = models.BooleanField(default=False, null=True, blank=True)
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="FormTourModule", on_delete=models.CASCADE, null=True, blank=True)
    first_document = models.BooleanField(default=False, null=True, blank=True)
    include_name_field = models.BooleanField(default=False, null=True, blank=True)
    ui_tour = models.BooleanField(default=False, null=True, blank=True)
    page_route = models.TextField(null=True, blank=True)
    dashboard_name = models.ForeignKey("frappe_app.Dashboard", related_name="FormTourDashboardName", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_VIEW_NAME = [
        ("Workspaces", "Workspaces"),
        ("List", "List"),
        ("Form", "Form"),
        ("Tree", "Tree"),
        ("Page", "Page"),
    ]
    view_name = models.CharField(choices=CHOICES_VIEW_NAME, max_length=255, null=True, blank=True)
    workspace_name = models.ForeignKey("frappe_app.Workspace", related_name="FormTourWorkspaceName", on_delete=models.CASCADE, null=True, blank=True)
    page_name = models.ForeignKey("cms_app.Page", related_name="FormTourPageName", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_LIST_NAME = [
        ("List", "List"),
        ("Report", "Report"),
        ("Dashboard", "Dashboard"),
        ("Kanban", "Kanban"),
        ("Gantt", "Gantt"),
        ("Calendar", "Calendar"),
        ("File", "File"),
        ("Image", "Image"),
        ("Inbox", "Inbox"),
        ("Map", "Map"),
    ]
    list_name = models.CharField(choices=CHOICES_LIST_NAME, max_length=255, default='List', null=True, blank=True)
    report_name = models.ForeignKey("frappe_app.Report", related_name="FormTourReportName", on_delete=models.CASCADE, null=True, blank=True)
    track_steps = models.BooleanField(default=False, null=True, blank=True)
    new_document_form = models.BooleanField(default=False, null=True, blank=True)
