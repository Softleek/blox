from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.address import Address
from frappe_app.filters.contacts.address import AddressFilter
from frappe_app.serializers.contacts.address import AddressSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AddressViewSet(GenericViewSet):
    queryset = Address.objects.all()
    filterset_class = AddressFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AddressSerializer

