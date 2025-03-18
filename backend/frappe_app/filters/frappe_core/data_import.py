import django_filters as filters
from frappe_app.models.frappe_core.data_import import DataImport

class DataImportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DataImport
        fields = ['id']

