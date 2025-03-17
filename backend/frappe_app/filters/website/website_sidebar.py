import django_filters as filters
from frappe_app.models.website.website_sidebar import WebsiteSidebar

class WebsiteSidebarFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteSidebar
        fields = ['id']

