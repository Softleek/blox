from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CustomDocPerm(BaseModel):
    role = models.ForeignKey("frappe_app.Role", related_name="CustomDocPermRole", on_delete=models.CASCADE, null=True, blank=True)
    if_owner = models.BooleanField(default=False, null=True, blank=True)
    permlevel = models.IntegerField(default=0, null=True, blank=True)
    read = models.BooleanField(default=True, null=True, blank=True)
    write = models.BooleanField(default=False, null=True, blank=True)
    create = models.BooleanField(default=False, null=True, blank=True)
    delete = models.BooleanField(default=False, null=True, blank=True)
    submit = models.BooleanField(default=False, null=True, blank=True)
    cancel = models.BooleanField(default=False, null=True, blank=True)
    amend = models.BooleanField(default=False, null=True, blank=True)
    report = models.BooleanField(default=False, null=True, blank=True)
    export = models.BooleanField(default=True, null=True, blank=True)
    custom_import = models.BooleanField(default=False, null=True, blank=True)
    share = models.BooleanField(default=False, null=True, blank=True)
    print = models.BooleanField(default=False, null=True, blank=True)
    email = models.BooleanField(default=False, null=True, blank=True)
    parent = models.CharField(max_length=255, null=True, blank=True)
    select = models.BooleanField(default=False, null=True, blank=True)
