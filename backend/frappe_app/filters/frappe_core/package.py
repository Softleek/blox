import django_filters as filters
from frappe_app.models.frappe_core.package import Package

class PackageFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = Package
        fields = ['id']

