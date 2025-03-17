import django_filters as filters
from frappe_app.models.website.website_route_meta import WebsiteRouteMeta

class WebsiteRouteMetaFilter(filters.FilterSet):
    id = filters.NumberFilter(label='ID')

    class Meta:
        model = WebsiteRouteMeta
        fields = ['id']

