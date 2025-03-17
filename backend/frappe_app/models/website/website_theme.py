from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebsiteTheme(BaseModel):
    theme = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="WebsiteThemeModule", on_delete=models.CASCADE, default='Website', null=True, blank=True)
    custom = models.BooleanField(default=True, null=True, blank=True)
    theme_scss = models.CharField(max_length=255, null=True, blank=True)
    theme_url = models.CharField(max_length=255, null=True, blank=True)
    js = models.CharField(max_length=255, null=True, blank=True)
    google_font = models.CharField(max_length=255, null=True, blank=True)
    font_size = models.CharField(max_length=255, null=True, blank=True)
    primary_color = models.ForeignKey("frappe_app.Color", related_name="WebsiteThemePrimaryColor", on_delete=models.CASCADE, null=True, blank=True)
    text_color = models.ForeignKey("frappe_app.Color", related_name="WebsiteThemeTextColor", on_delete=models.CASCADE, null=True, blank=True)
    dark_color = models.ForeignKey("frappe_app.Color", related_name="WebsiteThemeDarkColor", on_delete=models.CASCADE, null=True, blank=True)
    background_color = models.ForeignKey("frappe_app.Color", related_name="WebsiteThemeBackgroundColor", on_delete=models.CASCADE, null=True, blank=True)
    custom_scss = models.CharField(max_length=255, null=True, blank=True)
    light_color = models.ForeignKey("frappe_app.Color", related_name="WebsiteThemeLightColor", on_delete=models.CASCADE, null=True, blank=True)
    font_properties = models.CharField(max_length=255, default='wght@300;400;500;600;700;800', null=True, blank=True)
    button_rounded_corners = models.BooleanField(default=True, null=True, blank=True)
    button_shadows = models.BooleanField(default=False, null=True, blank=True)
    button_gradients = models.BooleanField(default=False, null=True, blank=True)
    custom_overrides = models.CharField(max_length=255, null=True, blank=True)
    ignored_apps = models.ManyToManyField("frappe_app.WebsiteThemeIgnoreApp", related_name="WebsiteThemeIgnoredApps", )
