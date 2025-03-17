import django_filters as filters
from frappe_app.models.website.portal_settings import PortalSettings

class PortalSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PortalSettings
        fields = ['id']

