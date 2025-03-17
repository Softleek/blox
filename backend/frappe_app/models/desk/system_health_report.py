from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class SystemHealthReport(SingletonModel):
    background_workers = models.ManyToManyField("frappe_app.SystemHealthReportWorkers", related_name="SystemHealthReportBackgroundWorkers", )
    total_background_workers = models.IntegerField(null=True, blank=True)
    scheduler_status = models.CharField(max_length=255, null=True, blank=True)
    queue_status = models.ManyToManyField("frappe_app.SystemHealthReportQueue", related_name="SystemHealthReportQueueStatus", )
    CHOICES_SOCKETIO_PING_CHECK = [
        ("Fail", "Fail"),
        ("Pass", "Pass"),
    ]
    socketio_ping_check = models.CharField(choices=CHOICES_SOCKETIO_PING_CHECK, max_length=255, default='Fail', null=True, blank=True)
    CHOICES_SOCKETIO_TRANSPORT_MODE = [
        ("Polling", "Polling"),
        ("Websocket", "Websocket"),
    ]
    socketio_transport_mode = models.CharField(choices=CHOICES_SOCKETIO_TRANSPORT_MODE, max_length=255, null=True, blank=True)
    failed_emails = models.IntegerField(null=True, blank=True)
    total_outgoing_emails = models.IntegerField(null=True, blank=True)
    pending_emails = models.IntegerField(null=True, blank=True)
    unhandled_emails = models.IntegerField(null=True, blank=True)
    handled_emails = models.IntegerField(null=True, blank=True)
    total_errors = models.IntegerField(null=True, blank=True)
    top_errors = models.ManyToManyField("frappe_app.SystemHealthReportErrors", related_name="SystemHealthReportTopErrors", )
    database = models.CharField(max_length=255, null=True, blank=True)
    db_storage_usage = models.FloatField(null=True, blank=True)
    top_db_tables = models.ManyToManyField("frappe_app.SystemHealthReportTables", related_name="SystemHealthReportTopDbTables", )
    database_version = models.CharField(max_length=255, null=True, blank=True)
    bufferpool_size = models.CharField(max_length=255, null=True, blank=True)
    binary_logging = models.CharField(max_length=255, null=True, blank=True)
    cache_keys = models.IntegerField(null=True, blank=True)
    cache_memory_usage = models.CharField(max_length=255, null=True, blank=True)
    backups_size = models.FloatField(null=True, blank=True)
    private_files_size = models.FloatField(null=True, blank=True)
    public_files_size = models.FloatField(null=True, blank=True)
    onsite_backups = models.IntegerField(null=True, blank=True)
    total_users = models.IntegerField(null=True, blank=True)
    new_users = models.IntegerField(null=True, blank=True)
    failed_logins = models.IntegerField(null=True, blank=True)
    active_sessions = models.IntegerField(null=True, blank=True)
    last_10_active_users = models.CharField(max_length=255, null=True, blank=True)
    background_jobs_check = models.CharField(max_length=255, null=True, blank=True)
    test_job_id = models.CharField(max_length=255, null=True, blank=True)
    failing_scheduled_jobs = models.ManyToManyField("frappe_app.SystemHealthReportFailingJobs", related_name="SystemHealthReportFailingScheduledJobs", )
    oldest_unscheduled_job = models.ForeignKey("frappe_app.ScheduledJobType", related_name="SystemHealthReportOldestUnscheduledJob", on_delete=models.CASCADE, null=True, blank=True)
