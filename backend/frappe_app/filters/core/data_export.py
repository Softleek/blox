import django_filters as filters
from frappe_app.models.core.data_export import DataExport

class DataExportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DataExport
        fields = ['id']

