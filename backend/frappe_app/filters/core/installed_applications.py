import django_filters as filters
from frappe_app.models.core.installed_applications import InstalledApplications

class InstalledApplicationsFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = InstalledApplications
        fields = ['id']

