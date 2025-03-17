import django_filters as filters
from frappe_app.models.website.portal_menu_item import PortalMenuItem

class PortalMenuItemFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = PortalMenuItem
        fields = ['id']

