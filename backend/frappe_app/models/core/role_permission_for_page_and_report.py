from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class RolePermissionForPageAndReport(SingletonModel):
    CHOICES_SET_ROLE_FOR = [
        ("Page", "Page"),
        ("Report", "Report"),
    ]
    set_role_for = models.CharField(choices=CHOICES_SET_ROLE_FOR, max_length=255, null=True, blank=True)
    page = models.ForeignKey("cms_app.Page", related_name="RolePermissionForPageAndReportPage", on_delete=models.CASCADE, null=True, blank=True)
    report = models.ForeignKey("frappe_app.Report", related_name="RolePermissionForPageAndReportReport", on_delete=models.CASCADE, null=True, blank=True)
    roles_html = models.TextField(null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="RolePermissionForPageAndReportRoles", )
    enable_prepared_report = models.BooleanField(default=False, null=True, blank=True)
