from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.navbar_item import NavbarItem
from frappe_app.filters.core.navbar_item import NavbarItemFilter
from frappe_app.serializers.core.navbar_item import NavbarItemSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class NavbarItemViewSet(GenericViewSet):
    queryset = NavbarItem.objects.all()
    filterset_class = NavbarItemFilter
    permission_classes = [HasGroupPermission]
    serializer_class = NavbarItemSerializer

