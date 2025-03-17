from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_route_redirect import WebsiteRouteRedirect
from frappe_app.filters.website.website_route_redirect import WebsiteRouteRedirectFilter
from frappe_app.serializers.website.website_route_redirect import WebsiteRouteRedirectSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteRouteRedirectViewSet(GenericViewSet):
    queryset = WebsiteRouteRedirect.objects.all()
    filterset_class = WebsiteRouteRedirectFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteRouteRedirectSerializer

