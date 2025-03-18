import django_filters as filters
from frappe_app.models.frappe_core.document_naming_settings import DocumentNamingSettings

class DocumentNamingSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DocumentNamingSettings
        fields = ['id']

