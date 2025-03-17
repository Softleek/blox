from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.custom.property_setter import PropertySetter
from frappe_app.filters.custom.property_setter import PropertySetterFilter
from frappe_app.serializers.custom.property_setter import PropertySetterSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PropertySetterViewSet(GenericViewSet):
    queryset = PropertySetter.objects.all()
    filterset_class = PropertySetterFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PropertySetterSerializer

