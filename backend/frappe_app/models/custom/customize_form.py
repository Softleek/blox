from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CustomizeForm(SingletonModel):
    CHOICES_NAMING_RULE = [
        ("Set by user", "Set by user"),
        ("By fieldname", "By fieldname"),
        ("By 'Naming Series' field", "By 'Naming Series' field"),
        ("Expression", "Expression"),
        ("Expression (old style)", "Expression (old style)"),
        ("Random", "Random"),
        ("By script", "By script"),
    ]
    naming_rule = models.CharField(choices=CHOICES_NAMING_RULE, max_length=255, null=True, blank=True)
    doc_type = models.ForeignKey("frappe_app.Doctype", related_name="CustomizeFormDocType", on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    default_print_format = models.ForeignKey("frappe_app.PrintFormat", related_name="CustomizeFormDefaultPrintFormat", on_delete=models.CASCADE, null=True, blank=True)
    max_attachments = models.IntegerField(null=True, blank=True)
    allow_copy = models.BooleanField(default=False, null=True, blank=True)
    istable = models.BooleanField(default=False, null=True, blank=True)
    editable_grid = models.BooleanField(default=False, null=True, blank=True)
    quick_entry = models.BooleanField(default=True, null=True, blank=True)
    track_changes = models.BooleanField(default=False, null=True, blank=True)
    title_field = models.CharField(max_length=255, null=True, blank=True)
    image_field = models.CharField(max_length=255, null=True, blank=True)
    search_fields = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_SORT_FIELD = [
        ("", ""),
    ]
    sort_field = models.CharField(choices=CHOICES_SORT_FIELD, max_length=255, null=True, blank=True)
    CHOICES_SORT_ORDER = [
        ("ASC", "ASC"),
        ("DESC", "DESC"),
    ]
    sort_order = models.CharField(choices=CHOICES_SORT_ORDER, max_length=255, null=True, blank=True)
    fields = models.ManyToManyField("frappe_app.CustomizeFormField", related_name="CustomizeFormFields", )
    track_views = models.BooleanField(default=False, null=True, blank=True)
    allow_auto_repeat = models.BooleanField(default=False, null=True, blank=True)
    allow_import = models.BooleanField(default=False, null=True, blank=True)
    subject_field = models.CharField(max_length=255, null=True, blank=True)
    sender_field = models.CharField(max_length=255, null=True, blank=True)
    email_append_to = models.BooleanField(default=False, null=True, blank=True)
    show_preview_popup = models.BooleanField(default=False, null=True, blank=True)
    links = models.ManyToManyField("frappe_app.DoctypeLink", related_name="CustomizeFormLinks", )
    actions = models.ManyToManyField("frappe_app.DoctypeAction", related_name="CustomizeFormActions", )
    default_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="CustomizeFormDefaultEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    autoname = models.CharField(max_length=255, null=True, blank=True)
    states = models.ManyToManyField("frappe_app.DoctypeState", related_name="CustomizeFormStates", )
    show_title_field_in_link = models.BooleanField(default=False, null=True, blank=True)
    translated_doctype = models.BooleanField(default=False, null=True, blank=True)
    make_attachments_public = models.BooleanField(default=False, null=True, blank=True)
    queue_in_background = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_DEFAULT_VIEW = [
        ("", ""),
    ]
    default_view = models.CharField(choices=CHOICES_DEFAULT_VIEW, max_length=255, null=True, blank=True)
    force_re_route_to_default_view = models.BooleanField(default=False, null=True, blank=True)
    is_calendar_and_gantt = models.BooleanField(default=False, null=True, blank=True)
    form_builder = models.TextField(null=True, blank=True)
    link_filters = models.JSONField(null=True, blank=True)
    sender_name_field = models.CharField(max_length=255, null=True, blank=True)
    grid_page_length = models.IntegerField(null=True, blank=True)
