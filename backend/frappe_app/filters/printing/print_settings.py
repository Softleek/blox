import django_filters as filters
from frappe_app.models.printing.print_settings import PrintSettings

class PrintSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PrintSettings
        fields = ['id']

