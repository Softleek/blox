import django_filters as filters
from frappe_app.models.core.domain_settings import DomainSettings

class DomainSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = DomainSettings
        fields = ['id']

