import django_filters as filters
from frappe_app.models.website.website_sidebar_item import WebsiteSidebarItem

class WebsiteSidebarItemFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteSidebarItem
        fields = ['id']

