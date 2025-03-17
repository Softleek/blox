from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class WebPage(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    slideshow = models.ForeignKey("frappe_app.WebsiteSlideshow", related_name="WebPageSlideshow", on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=True, null=True, blank=True)
    show_title = models.BooleanField(default=False, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    CHOICES_CONTENT_TYPE = [
        ("Rich Text", "Rich Text"),
        ("Markdown", "Markdown"),
        ("HTML", "HTML"),
        ("Page Builder", "Page Builder"),
        ("Slideshow", "Slideshow"),
    ]
    content_type = models.CharField(choices=CHOICES_CONTENT_TYPE, max_length=255, default='Page Builder', null=True, blank=True)
    main_section = models.CharField(max_length=255, null=True, blank=True)
    main_section_md = models.TextField(null=True, blank=True)
    main_section_html = models.TextField(null=True, blank=True)
    javascript = models.CharField(max_length=255, null=True, blank=True)
    insert_style = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_TEXT_ALIGN = [
        ("Left", "Left"),
        ("Center", "Center"),
        ("Right", "Right"),
    ]
    text_align = models.CharField(choices=CHOICES_TEXT_ALIGN, max_length=255, null=True, blank=True)
    css = models.CharField(max_length=255, null=True, blank=True)
    show_sidebar = models.BooleanField(default=False, null=True, blank=True)
    website_sidebar = models.ForeignKey("frappe_app.WebsiteSidebar", related_name="WebPageWebsiteSidebar", on_delete=models.CASCADE, null=True, blank=True)
    enable_comments = models.BooleanField(default=False, null=True, blank=True)
    idx = models.IntegerField(null=True, blank=True)
    header = models.TextField(null=True, blank=True)
    breadcrumbs = models.CharField(max_length=255, null=True, blank=True)
    set_meta_tags = models.CharField(max_length=255, null=True, blank=True)
    dynamic_template = models.BooleanField(default=False, null=True, blank=True)
    page_blocks = models.ManyToManyField("frappe_app.WebPageBlock", related_name="WebPagePageBlocks", )
    full_width = models.BooleanField(default=True, null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_image = models.CharField(max_length=255, null=True, blank=True)
    dynamic_route = models.BooleanField(default=False, null=True, blank=True)
    context_script = models.CharField(max_length=255, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="WebPageModule", on_delete=models.CASCADE, null=True, blank=True)
