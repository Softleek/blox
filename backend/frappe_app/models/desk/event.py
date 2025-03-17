from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class Event(BaseModel):
    subject = models.TextField(null=True, blank=True)
    CHOICES_EVENT_CATEGORY = [
        ("Event", "Event"),
        ("Meeting", "Meeting"),
        ("Call", "Call"),
        ("Sent/Received Email", "Sent/Received Email"),
        ("Other", "Other"),
    ]
    event_category = models.CharField(choices=CHOICES_EVENT_CATEGORY, max_length=255, null=True, blank=True)
    CHOICES_EVENT_TYPE = [
        ("Private", "Private"),
        ("Public", "Public"),
    ]
    event_type = models.CharField(choices=CHOICES_EVENT_TYPE, max_length=255, null=True, blank=True)
    send_reminder = models.BooleanField(default=True, null=True, blank=True)
    repeat_this_event = models.BooleanField(default=False, null=True, blank=True)
    starts_on = models.DateTimeField(null=True, blank=True)
    ends_on = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_REPEAT_ON = [
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Half Yearly", "Half Yearly"),
        ("Yearly", "Yearly"),
    ]
    repeat_on = models.CharField(choices=CHOICES_REPEAT_ON, max_length=255, null=True, blank=True)
    repeat_till = models.DateField(null=True, blank=True)
    monday = models.BooleanField(default=False, null=True, blank=True)
    tuesday = models.BooleanField(default=False, null=True, blank=True)
    wednesday = models.BooleanField(default=False, null=True, blank=True)
    thursday = models.BooleanField(default=False, null=True, blank=True)
    friday = models.BooleanField(default=False, null=True, blank=True)
    saturday = models.BooleanField(default=False, null=True, blank=True)
    sunday = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    event_participants = models.ManyToManyField("frappe_app.EventParticipants", related_name="EventEventParticipants", )
    CHOICES_STATUS = [
        ("Open", "Open"),
        ("Completed", "Completed"),
        ("Closed", "Closed"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(choices=CHOICES_STATUS, max_length=255, default='Open', null=True, blank=True)
    custom_google_calendar = models.CharField(max_length=255, null=True, blank=True)
    google_calendar_event_id = models.CharField(max_length=255, null=True, blank=True)
    sync_with_google_calendar = models.BooleanField(default=False, null=True, blank=True)
    google_calendar = models.ForeignKey("frappe_app.GoogleCalendar", related_name="EventGoogleCalendar", on_delete=models.CASCADE, null=True, blank=True)
    pulled_from_google_calendar = models.BooleanField(default=False, null=True, blank=True)
    sender = models.CharField(max_length=255, null=True, blank=True)
    add_video_conferencing = models.BooleanField(default=False, null=True, blank=True)
    google_meet_link = models.CharField(max_length=255, null=True, blank=True)
