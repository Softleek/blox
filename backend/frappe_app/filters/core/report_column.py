import django_filters as filters
from frappe_app.models.core.report_column import ReportColumn

class ReportColumnFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = ReportColumn
        fields = ['id']

