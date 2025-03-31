from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.website.website_sidebar_item import WebsiteSidebarItem
from frappe_app.filters.website.website_sidebar_item import WebsiteSidebarItemFilter
from frappe_app.serializers.website.website_sidebar_item import WebsiteSidebarItemSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebsiteSidebarItemViewSet(GenericViewSet):
    queryset = WebsiteSidebarItem.objects.all()
    filterset_class = WebsiteSidebarItemFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebsiteSidebarItemSerializer

    filterset_class = WebsiteSidebarItemFilter
