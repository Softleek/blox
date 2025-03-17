from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class AboutUsSettings(SingletonModel):
    company_introduction = models.CharField(max_length=255, null=True, blank=True)
    company_history_heading = models.CharField(max_length=255, null=True, blank=True)
    company_history = models.ManyToManyField("frappe_app.CompanyHistory", related_name="AboutUsSettingsCompanyHistory", )
    team_members_heading = models.CharField(max_length=255, null=True, blank=True)
    team_members = models.ManyToManyField("frappe_app.AboutUsTeamMember", related_name="AboutUsSettingsTeamMembers", )
    footer = models.CharField(max_length=255, null=True, blank=True)
    page_title = models.CharField(max_length=255, null=True, blank=True)
    team_members_subtitle = models.TextField(null=True, blank=True)
