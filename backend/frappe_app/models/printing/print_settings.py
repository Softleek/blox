from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PrintSettings(SingletonModel):
    send_print_as_pdf = models.BooleanField(default=True, null=True, blank=True)
    repeat_header_footer = models.BooleanField(default=True, null=True, blank=True)
    CHOICES_PDF_PAGE_SIZE = [
        ("A0", "A0"),
        ("A1", "A1"),
        ("A2", "A2"),
        ("A3", "A3"),
        ("A4", "A4"),
        ("A5", "A5"),
        ("A6", "A6"),
        ("A7", "A7"),
        ("A8", "A8"),
        ("A9", "A9"),
        ("B0", "B0"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("B3", "B3"),
        ("B4", "B4"),
        ("B5", "B5"),
        ("B6", "B6"),
        ("B7", "B7"),
        ("B8", "B8"),
        ("B9", "B9"),
        ("B10", "B10"),
        ("C5E", "C5E"),
        ("Comm10E", "Comm10E"),
        ("DLE", "DLE"),
        ("Executive", "Executive"),
        ("Folio", "Folio"),
        ("Ledger", "Ledger"),
        ("Legal", "Legal"),
        ("Letter", "Letter"),
        ("Tabloid", "Tabloid"),
        ("Custom", "Custom"),
    ]
    pdf_page_size = models.CharField(choices=CHOICES_PDF_PAGE_SIZE, max_length=255, default='A4', null=True, blank=True)
    with_letterhead = models.BooleanField(default=True, null=True, blank=True)
    allow_print_for_draft = models.BooleanField(default=True, null=True, blank=True)
    add_draft_heading = models.BooleanField(default=True, null=True, blank=True)
    allow_page_break_inside_tables = models.BooleanField(default=False, null=True, blank=True)
    allow_print_for_cancelled = models.BooleanField(default=False, null=True, blank=True)
    enable_print_server = models.BooleanField(default=False, null=True, blank=True)
    enable_raw_printing = models.BooleanField(default=False, null=True, blank=True)
    print_style = models.ForeignKey("frappe_app.PrintStyle", related_name="PrintSettingsPrintStyle", on_delete=models.CASCADE, default='Redesign', null=True, blank=True)
    print_style_preview = models.TextField(null=True, blank=True)
    CHOICES_FONT = [
        ("Default", "Default"),
        ("Helvetica Neue", "Helvetica Neue"),
        ("Arial", "Arial"),
        ("Helvetica", "Helvetica"),
        ("Inter", "Inter"),
        ("Verdana", "Verdana"),
        ("Monospace", "Monospace"),
    ]
    font = models.CharField(choices=CHOICES_FONT, max_length=255, default='Default', null=True, blank=True)
    font_size = models.FloatField(null=True, blank=True)
    pdf_page_height = models.FloatField(null=True, blank=True)
    pdf_page_width = models.FloatField(null=True, blank=True)
