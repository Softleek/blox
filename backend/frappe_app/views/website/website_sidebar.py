from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.website_sidebar import WebsiteSidebar
from frappe_app.filters.website.website_sidebar import WebsiteSidebarFilter
from frappe_app.serializers.website.website_sidebar import WebsiteSidebarSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSidebarViewSet(GenericViewSet):
    queryset = WebsiteSidebar.objects.all()
    filterset_class = WebsiteSidebarFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSidebarSerializer

