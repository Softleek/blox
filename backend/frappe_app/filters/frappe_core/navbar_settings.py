import django_filters as filters
from frappe_app.models.frappe_core.navbar_settings import NavbarSettings

class NavbarSettingsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NavbarSettings
        fields = ['id']

