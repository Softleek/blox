import django_filters as filters
from frappe_app.models.frappe_core.report_filter import ReportFilter

class ReportFilterFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ReportFilter
        fields = ['id']

