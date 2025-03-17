import django_filters as filters
from frappe_app.models.website.website_route_redirect import WebsiteRouteRedirect

class WebsiteRouteRedirectFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteRouteRedirect
        fields = ['id']

