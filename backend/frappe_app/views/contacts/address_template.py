from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.contacts.address_template import AddressTemplate
from frappe_app.filters.contacts.address_template import AddressTemplateFilter
from frappe_app.serializers.contacts.address_template import AddressTemplateSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AddressTemplateViewSet(GenericViewSet):
    queryset = AddressTemplate.objects.all()
    filterset_class = AddressTemplateFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AddressTemplateSerializer

