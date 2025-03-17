from django.db import models
from multiselectfield import MultiSelectField
from core.models.template import BaseModel, SingletonModel
import uuid
import os
from django.conf import settings

class DashboardChart(BaseModel):
    chart_name = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_CHART_TYPE = [
        ("Count", "Count"),
        ("Sum", "Sum"),
        ("Average", "Average"),
        ("Group By", "Group By"),
        ("Custom", "Custom"),
        ("Report", "Report"),
    ]
    chart_type = models.CharField(choices=CHOICES_CHART_TYPE, max_length=255, null=True, blank=True)
    source = models.ForeignKey("frappe_app.DashboardChartSource", related_name="DashboardChartSource", on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.ForeignKey("frappe_app.Doctype", related_name="DashboardChartDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    CHOICES_BASED_ON = [
        ("", ""),
    ]
    based_on = models.CharField(choices=CHOICES_BASED_ON, max_length=255, null=True, blank=True)
    CHOICES_VALUE_BASED_ON = [
        ("", ""),
    ]
    value_based_on = models.CharField(choices=CHOICES_VALUE_BASED_ON, max_length=255, null=True, blank=True)
    CHOICES_TIMESPAN = [
        ("Last Year", "Last Year"),
        ("Last Quarter", "Last Quarter"),
        ("Last Month", "Last Month"),
        ("Last Week", "Last Week"),
        ("Select Date Range", "Select Date Range"),
    ]
    timespan = models.CharField(choices=CHOICES_TIMESPAN, max_length=255, null=True, blank=True)
    CHOICES_TIME_INTERVAL = [
        ("Yearly", "Yearly"),
        ("Quarterly", "Quarterly"),
        ("Monthly", "Monthly"),
        ("Weekly", "Weekly"),
        ("Daily", "Daily"),
    ]
    time_interval = models.CharField(choices=CHOICES_TIME_INTERVAL, max_length=255, null=True, blank=True)
    timeseries = models.BooleanField(default=False, null=True, blank=True)
    filters_json = models.CharField(max_length=255, null=True, blank=True)
    CHOICES_TYPE = [
        ("Line", "Line"),
        ("Bar", "Bar"),
        ("Percentage", "Percentage"),
        ("Pie", "Pie"),
        ("Donut", "Donut"),
        ("Heatmap", "Heatmap"),
    ]
    type = models.CharField(choices=CHOICES_TYPE, max_length=255, default='Line', null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    last_synced_on = models.DateTimeField(null=True, blank=True)
    CHOICES_GROUP_BY_BASED_ON = [
        ("", ""),
    ]
    group_by_based_on = models.CharField(choices=CHOICES_GROUP_BY_BASED_ON, max_length=255, null=True, blank=True)
    CHOICES_GROUP_BY_TYPE = [
        ("Count", "Count"),
        ("Sum", "Sum"),
        ("Average", "Average"),
    ]
    group_by_type = models.CharField(choices=CHOICES_GROUP_BY_TYPE, max_length=255, default='Count', null=True, blank=True)
    CHOICES_AGGREGATE_FUNCTION_BASED_ON = [
        ("", ""),
    ]
    aggregate_function_based_on = models.CharField(choices=CHOICES_AGGREGATE_FUNCTION_BASED_ON, max_length=255, null=True, blank=True)
    number_of_groups = models.IntegerField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    CHOICES_X_FIELD = [
        ("", ""),
    ]
    x_field = models.CharField(choices=CHOICES_X_FIELD, max_length=255, null=True, blank=True)
    report_name = models.ForeignKey("frappe_app.Report", related_name="DashboardChartReportName", on_delete=models.CASCADE, null=True, blank=True)
    y_axis = models.ManyToManyField("frappe_app.DashboardChartField", related_name="DashboardChartYAxis", )
    custom_options = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=False, null=True, blank=True)
    CHOICES_HEATMAP_YEAR = [
        ("", ""),
    ]
    heatmap_year = models.CharField(choices=CHOICES_HEATMAP_YEAR, max_length=255, null=True, blank=True)
    is_standard = models.BooleanField(default=False, null=True, blank=True)
    module = models.ForeignKey("frappe_app.ModuleDef", related_name="DashboardChartModule", on_delete=models.CASCADE, null=True, blank=True)
    dynamic_filters_json = models.CharField(max_length=255, null=True, blank=True)
    use_report_chart = models.BooleanField(default=False, null=True, blank=True)
    parent_document_type = models.ForeignKey("frappe_app.Doctype", related_name="DashboardChartParentDocumentType", on_delete=models.CASCADE, null=True, blank=True)
    roles = models.ManyToManyField("frappe_app.HasRole", related_name="DashboardChartRoles", )
    currency = models.ForeignKey("frappe_app.Currency", related_name="DashboardChartCurrency", on_delete=models.CASCADE, null=True, blank=True)
