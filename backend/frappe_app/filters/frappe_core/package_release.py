import django_filters as filters
from frappe_app.models.frappe_core.package_release import PackageRelease

class PackageReleaseFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PackageRelease
        fields = ['id']

