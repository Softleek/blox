import django_filters as filters
from frappe_app.models.email.auto_email_report import AutoEmailReport

class AutoEmailReportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AutoEmailReport
        fields = ['id']

