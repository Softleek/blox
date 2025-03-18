import django_filters as filters
from frappe_app.models.frappe_core.amended_document_naming_settings import AmendedDocumentNamingSettings

class AmendedDocumentNamingSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = AmendedDocumentNamingSettings
        fields = ['id']

