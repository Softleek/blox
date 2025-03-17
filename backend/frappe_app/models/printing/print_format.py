from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class PrintFormat(BaseModel):
    doc_type = models.ForeignKey("frappe_app.Doctype", related_name="PrintFormatDocType", on_delete=models.CASCADE, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="PrintFormatModule", on_delete=models.CASCADE, null=True, blank=True)
    disabled = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_STANDARD = [
        ("No", "No"),
        ("Yes", "Yes"),
    ]
    standard = models.CharField(choices=CHOICES_STANDARD, max_length=255, default='No', null=True, blank=True)
    custom_format = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_PRINT_FORMAT_TYPE = [
        ("Jinja", "Jinja"),
        ("JS", "JS"),
    ]
    print_format_type = models.CharField(choices=CHOICES_PRINT_FORMAT_TYPE, max_length=255, default='Jinja', null=True, blank=True)
    raw_printing = models.BooleanField(default=False, null=True, blank=True)
    html = models.CharField(max_length=255, null=True, blank=True)
    raw_commands = models.CharField(max_length=255, null=True, blank=True)
    align_labels_right = models.BooleanField(default=False, null=True, blank=True)
    show_section_headings = models.BooleanField(default=False, null=True, blank=True)
    line_breaks = models.BooleanField(default=False, null=True, blank=True)
    default_print_language = models.ForeignKey("frappe_app.Language", related_name="PrintFormatDefaultPrintLanguage", on_delete=models.CASCADE, null=True, blank=True)
    font = models.CharField(max_length=255, null=True, blank=True)
    css = models.CharField(max_length=255, null=True, blank=True)
    custom_html_help = models.TextField(null=True, blank=True)
    print_format_help = models.TextField(null=True, blank=True)
    format_data = models.CharField(max_length=255, null=True, blank=True)
    print_format_builder = models.BooleanField(default=False, null=True, blank=True)
    absolute_value = models.BooleanField(default=False, null=True, blank=True)
    print_format_builder_beta = models.BooleanField(default=False, null=True, blank=True)
    margin_top = models.FloatField(default=15.0, null=True, blank=True)
    margin_bottom = models.FloatField(default=15.0, null=True, blank=True)
    margin_left = models.FloatField(default=15.0, null=True, blank=True)
    margin_right = models.FloatField(default=15.0, null=True, blank=True)
    font_size = models.IntegerField(default=14, null=True, blank=True)
    CHOICES_PAGE_NUMBER = [
        ("Hide", "Hide"),
        ("Top Left", "Top Left"),
        ("Top Center", "Top Center"),
        ("Top Right", "Top Right"),
        ("Bottom Left", "Bottom Left"),
        ("Bottom Center", "Bottom Center"),
        ("Bottom Right", "Bottom Right"),
    ]
    page_number = models.CharField(choices=CHOICES_PAGE_NUMBER, max_length=255, default='Hide', null=True, blank=True)
    CHOICES_PDF_GENERATOR = [
        ("wkhtmltopdf", "wkhtmltopdf"),
    ]
    pdf_generator = models.CharField(choices=CHOICES_PDF_GENERATOR, max_length=255, default='wkhtmltopdf', null=True, blank=True)
