from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.website.portal_menu_item import PortalMenuItem
from frappe_app.filters.website.portal_menu_item import PortalMenuItemFilter
from frappe_app.serializers.website.portal_menu_item import PortalMenuItemSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PortalMenuItemViewSet(GenericViewSet):
    queryset = PortalMenuItem.objects.all()
    filterset_class = PortalMenuItemFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PortalMenuItemSerializer

