from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class CustomizeFormField(BaseModel):
    label = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_FIELDTYPE = [
        ("Autocomplete", "Autocomplete"),
        ("Attach", "Attach"),
        ("Attach Image", "Attach Image"),
        ("Barcode", "Barcode"),
        ("Button", "Button"),
        ("Check", "Check"),
        ("Code", "Code"),
        ("Color", "Color"),
        ("Column Break", "Column Break"),
        ("Currency", "Currency"),
        ("Data", "Data"),
        ("Date", "Date"),
        ("Datetime", "Datetime"),
        ("Duration", "Duration"),
        ("Dynamic Link", "Dynamic Link"),
        ("Float", "Float"),
        ("Fold", "Fold"),
        ("Geolocation", "Geolocation"),
        ("Heading", "Heading"),
        ("HTML", "HTML"),
        ("HTML Editor", "HTML Editor"),
        ("Icon", "Icon"),
        ("Image", "Image"),
        ("Int", "Int"),
        ("JSON", "JSON"),
        ("Link", "Link"),
        ("Long Text", "Long Text"),
        ("Markdown Editor", "Markdown Editor"),
        ("Password", "Password"),
        ("Percent", "Percent"),
        ("Phone", "Phone"),
        ("Rating", "Rating"),
        ("Read Only", "Read Only"),
        ("Section Break", "Section Break"),
        ("Select", "Select"),
        ("Signature", "Signature"),
        ("Small Text", "Small Text"),
        ("Tab Break", "Tab Break"),
        ("Table", "Table"),
        ("Table MultiSelect", "Table MultiSelect"),
        ("Text", "Text"),
        ("Text Editor", "Text Editor"),
        ("Time", "Time"),
    ]
    fieldtype = models.CharField(choices=CHOICES_FIELDTYPE, max_length=255, default='Data', null=True, blank=True)
    fieldname = models.CharField(max_length=255, null=True, blank=True)
    reqd = models.BooleanField(default=False, null=True, blank=True)
    unique = models.BooleanField(default=False, null=True, blank=True)
    is_virtual = models.BooleanField(default=False, null=True, blank=True)
    in_list_view = models.BooleanField(default=False, null=True, blank=True)
    in_standard_filter = models.BooleanField(default=False, null=True, blank=True)
    in_global_search = models.BooleanField(default=False, null=True, blank=True)
    bold = models.BooleanField(default=False, null=True, blank=True)
    translatable = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_PRECISION = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
    ]
    precision = models.CharField(choices=CHOICES_PRECISION, max_length=255, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    options = models.TextField(null=True, blank=True)
    fetch_from = models.TextField(null=True, blank=True)
    fetch_if_empty = models.BooleanField(default=False, null=True, blank=True)
    depends_on = models.CharField(max_length=255, null=True, blank=True)
    permlevel = models.IntegerField(default=0, null=True, blank=True)
    hidden = models.BooleanField(default=False, null=True, blank=True)
    read_only = models.BooleanField(default=False, null=True, blank=True)
    collapsible = models.BooleanField(default=False, null=True, blank=True)
    allow_bulk_edit = models.BooleanField(default=False, null=True, blank=True)
    collapsible_depends_on = models.CharField(max_length=255, null=True, blank=True)
    ignore_user_permissions = models.BooleanField(default=False, null=True, blank=True)
    allow_on_submit = models.BooleanField(default=False, null=True, blank=True)
    report_hide = models.BooleanField(default=False, null=True, blank=True)
    remember_last_selected_value = models.BooleanField(default=False, null=True, blank=True)
    default = models.TextField(null=True, blank=True)
    in_filter = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    print_hide = models.BooleanField(default=False, null=True, blank=True)
    print_hide_if_no_value = models.BooleanField(default=False, null=True, blank=True)
    print_width = models.CharField(max_length=255, null=True, blank=True)
    columns = models.IntegerField(null=True, blank=True)
    width = models.CharField(max_length=255, null=True, blank=True)
    is_custom_field = models.BooleanField(default=False, null=True, blank=True)
    allow_in_quick_entry = models.BooleanField(default=False, null=True, blank=True)
    mandatory_depends_on = models.CharField(max_length=255, null=True, blank=True)
    read_only_depends_on = models.CharField(max_length=255, null=True, blank=True)
    in_preview = models.BooleanField(default=False, null=True, blank=True)
    hide_seconds = models.BooleanField(default=False, null=True, blank=True)
    hide_days = models.BooleanField(default=False, null=True, blank=True)
    hide_border = models.BooleanField(default=False, null=True, blank=True)
    non_negative = models.BooleanField(default=False, null=True, blank=True)
    show_dashboard = models.BooleanField(default=False, null=True, blank=True)
    no_copy = models.BooleanField(default=False, null=True, blank=True)
    is_system_generated = models.BooleanField(default=False, null=True, blank=True)
    ignore_xss_filter = models.BooleanField(default=False, null=True, blank=True)
    sort_options = models.BooleanField(default=False, null=True, blank=True)
    link_filters = models.JSONField(null=True, blank=True)
    placeholder = models.CharField(max_length=255, null=True, blank=True)
