import django_filters as filters
from frappe_app.models.core.version import Version

class VersionFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Version
        fields = ['id']

