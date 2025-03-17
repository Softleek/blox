from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Currency(BaseModel):
    currency_name = models.CharField(max_length=255, null=True, blank=True)
    enabled = models.BooleanField(default=False, null=True, blank=True)
    fraction = models.CharField(max_length=255, null=True, blank=True)
    fraction_units = models.IntegerField(null=True, blank=True)
    smallest_currency_fraction_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    symbol = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_NUMBER_FORMAT = [
        ("#,###.##", "#,###.##"),
        ("#.###,##", "#.###,##"),
        ("# ###.##", "# ###.##"),
        ("# ###,##", "# ###,##"),
        ("#'###.##", "#'###.##"),
        ("#, ###.##", "#, ###.##"),
        ("#,##,###.##", "#,##,###.##"),
        ("#,###.###", "#,###.###"),
        ("#.###", "#.###"),
        ("#,###", "#,###"),
    ]
    number_format = models.CharField(choices=CHOICES_NUMBER_FORMAT, max_length=255, null=True, blank=True)
    symbol_on_right = models.BooleanField(default=False, null=True, blank=True)
