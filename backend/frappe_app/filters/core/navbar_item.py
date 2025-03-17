import django_filters as filters
from frappe_app.models.core.navbar_item import NavbarItem

class NavbarItemFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = NavbarItem
        fields = ['id']

