import django_filters as filters
from frappe_app.models.core.installed_application import InstalledApplication

class InstalledApplicationFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = InstalledApplication
        fields = ['id']

