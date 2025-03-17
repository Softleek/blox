from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DocType(BaseModel):
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="DocTypeModule", on_delete=models.CASCADE, null=True, blank=True)
    is_submittable = models.BooleanField(default=False, null=True, blank=True)
    istable = models.BooleanField(default=False, null=True, blank=True)
    issingle = models.BooleanField(default=False, null=True, blank=True)
    editable_grid = models.BooleanField(default=True, null=True, blank=True)
    quick_entry = models.BooleanField(default=False, null=True, blank=True)
    track_changes = models.BooleanField(default=False, null=True, blank=True)
    track_seen = models.BooleanField(default=False, null=True, blank=True)
    track_views = models.BooleanField(default=False, null=True, blank=True)
    custom = models.BooleanField(default=False, null=True, blank=True)
    beta = models.BooleanField(default=False, null=True, blank=True)
    fields = models.ManyToManyField("frappe_app.Docfield", related_name="DocTypeFields", )
    autoname = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_field = models.CharField(max_length=255, null=True, blank=True)
    timeline_field = models.CharField(max_length=255, null=True, blank=True)
    max_attachments = models.IntegerField(null=True, blank=True)
    hide_toolbar = models.BooleanField(default=False, null=True, blank=True)
    allow_copy = models.BooleanField(default=False, null=True, blank=True)
    allow_rename = models.BooleanField(default=True, null=True, blank=True)
    allow_import = models.BooleanField(default=False, null=True, blank=True)
    allow_events_in_timeline = models.BooleanField(default=False, null=True, blank=True)
    allow_auto_repeat = models.BooleanField(default=False, null=True, blank=True)
    title_field = models.CharField(max_length=255, null=True, blank=True)
    search_fields = models.CharField(max_length=255, null=True, blank=True)
    default_print_format = models.CharField(max_length=255, null=True, blank=True)
    sort_field = models.CharField(max_length=255, default='creation', null=True, blank=True)
    CHOICES_SORT_ORDER = [
        ("ASC", "ASC"),
        ("DESC", "DESC"),
    ]
    sort_order = models.CharField(choices=CHOICES_SORT_ORDER, max_length=255, default='DESC', null=True, blank=True)
    CHOICES_DOCUMENT_TYPE = [
        ("Document", "Document"),
        ("Setup", "Setup"),
        ("System", "System"),
        ("Other", "Other"),
    ]
    document_type = models.CharField(choices=CHOICES_DOCUMENT_TYPE, max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    show_preview_popup = models.BooleanField(default=False, null=True, blank=True)
    show_name_in_global_search = models.BooleanField(default=False, null=True, blank=True)
    permissions = models.ManyToManyField("frappe_app.Docperm", related_name="DocTypePermissions", )
    restrict_to_domain = models.ForeignKey("frappe_app.Domain", related_name="DocTypeRestrictToDomain", on_delete=models.CASCADE, null=True, blank=True)
    read_only = models.BooleanField(default=False, null=True, blank=True)
    in_create = models.BooleanField(default=False, null=True, blank=True)
    has_web_view = models.BooleanField(default=False, null=True, blank=True)
    allow_guest_to_view = models.BooleanField(default=False, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    is_published_field = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ENGINE = [
        ("InnoDB", "InnoDB"),
        ("MyISAM", "MyISAM"),
    ]
    engine = models.CharField(choices=CHOICES_ENGINE, max_length=255, default='InnoDB', null=True, blank=True)
    is_tree = models.BooleanField(default=False, null=True, blank=True)
    nsm_parent_field = models.CharField(max_length=255, null=True, blank=True)
    documentation = models.CharField(max_length=255, null=True, blank=True)
    actions = models.ManyToManyField("frappe_app.DoctypeAction", related_name="DocTypeActions", )
    links = models.ManyToManyField("frappe_app.DoctypeLink", related_name="DocTypeLinks", )
    subject_field = models.CharField(max_length=255, null=True, blank=True)
    sender_field = models.CharField(max_length=255, null=True, blank=True)
    email_append_to = models.BooleanField(default=False, null=True, blank=True)
    index_web_pages_for_search = models.BooleanField(default=True, null=True, blank=True)
    is_virtual = models.BooleanField(default=False, null=True, blank=True)
    default_email_template = models.ForeignKey("frappe_app.EmailTemplate", related_name="DocTypeDefaultEmailTemplate", on_delete=models.CASCADE, null=True, blank=True)
    website_search_field = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_NAMING_RULE = [
        ("Set by user", "Set by user"),
        ("Autoincrement", "Autoincrement"),
        ("By fieldname", "By fieldname"),
        ("By 'Naming Series' field", "By 'Naming Series' field"),
        ("Expression", "Expression"),
        ("Expression (old style)", "Expression (old style)"),
        ("Random", "Random"),
        ("UUID", "UUID"),
        ("By script", "By script"),
    ]
    naming_rule = models.CharField(choices=CHOICES_NAMING_RULE, max_length=255, null=True, blank=True)
    migration_hash = models.CharField(max_length=255, null=True, blank=True)
    states = models.ManyToManyField("frappe_app.DoctypeState", related_name="DocTypeStates", )
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
    sender_name_field = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_ROW_FORMAT = [
        ("Dynamic", "Dynamic"),
        ("Compressed", "Compressed"),
    ]
    row_format = models.CharField(choices=CHOICES_ROW_FORMAT, max_length=255, default='Dynamic', null=True, blank=True)
    grid_page_length = models.IntegerField(default=50, null=True, blank=True)
