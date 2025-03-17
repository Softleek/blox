from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Language(BaseModel):
    language_code = models.CharField(max_length=255, null=True, blank=True)
    language_name = models.CharField(max_length=255, null=True, blank=True)
    flag = models.CharField(max_length=255, null=True, blank=True)
    based_on = models.ForeignKey("frappe_app.Language", related_name="LanguageBasedOn", on_delete=models.CASCADE, null=True, blank=True)
    enabled = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_DATE_FORMAT = [
        ("yyyy-mm-dd", "yyyy-mm-dd"),
        ("dd-mm-yyyy", "dd-mm-yyyy"),
        ("dd/mm/yyyy", "dd/mm/yyyy"),
        ("dd.mm.yyyy", "dd.mm.yyyy"),
        ("mm/dd/yyyy", "mm/dd/yyyy"),
        ("mm-dd-yyyy", "mm-dd-yyyy"),
    ]
    date_format = models.CharField(choices=CHOICES_DATE_FORMAT, max_length=255, null=True, blank=True)
    CHOICES_TIME_FORMAT = [
        ("HH:mm:ss", "HH:mm:ss"),
        ("HH:mm", "HH:mm"),
    ]
    time_format = models.CharField(choices=CHOICES_TIME_FORMAT, max_length=255, null=True, blank=True)
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
    CHOICES_FIRST_DAY_OF_THE_WEEK = [
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    ]
    first_day_of_the_week = models.CharField(choices=CHOICES_FIRST_DAY_OF_THE_WEEK, max_length=255, null=True, blank=True)
