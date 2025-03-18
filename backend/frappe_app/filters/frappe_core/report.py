import django_filters as filters
from frappe_app.models.frappe_core.report import Report

class ReportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Report
        fields = ['id']

