import django_filters as filters
from frappe_app.models.core.package_import import PackageImport

class PackageImportFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PackageImport
        fields = ['id']

