import django_filters as filters
from frappe_app.models.frappe_core.data_import_log import DataImportLog

class DataImportLogFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DataImportLog
        fields = ['id']

