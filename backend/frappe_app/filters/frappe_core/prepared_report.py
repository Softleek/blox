import django_filters as filters
from frappe_app.models.frappe_core.prepared_report import PreparedReport

class PreparedReportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PreparedReport
        fields = ['id']

