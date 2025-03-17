from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class EnergyPointLog(BaseModel):
    user = models.ForeignKey("frappe_app.User", related_name="EnergyPointLogUser", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_TYPE = [
        ("Auto", "Auto"),
        ("Appreciation", "Appreciation"),
        ("Criticism", "Criticism"),
        ("Review", "Review"),
        ("Revert", "Revert"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, null=True, blank=True)
    rule = models.ForeignKey("frappe_app.EnergyPointRule", related_name="EnergyPointLogRule", on_delete=models.CASCADE, null=True, blank=True)
    reference_doctype = models.ForeignKey("frappe_app.Doctype", related_name="EnergyPointLogReferenceDoctype", on_delete=models.CASCADE, null=True, blank=True)
    reference_name = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    reverted = models.BooleanField(default=False, null=True, blank=True)
    revert_of = models.ForeignKey("frappe_app.EnergyPointLog", related_name="EnergyPointLogRevertOf", on_delete=models.CASCADE, null=True, blank=True)
    seen = models.BooleanField(default=False, null=True, blank=True)
