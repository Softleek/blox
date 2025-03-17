from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_route_meta import WebsiteRouteMeta
from frappe_app.filters.website.website_route_meta import WebsiteRouteMetaFilter
from frappe_app.serializers.website.website_route_meta import WebsiteRouteMetaSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteRouteMetaViewSet(GenericViewSet):
    queryset = WebsiteRouteMeta.objects.all()
    filterset_class = WebsiteRouteMetaFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteRouteMetaSerializer

