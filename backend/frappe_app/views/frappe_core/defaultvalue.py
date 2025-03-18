from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.defaultvalue import DefaultValue
from frappe_app.filters.frappe_core.defaultvalue import DefaultValueFilter
from frappe_app.serializers.frappe_core.defaultvalue import DefaultValueSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class DefaultValueViewSet(GenericViewSet):
    queryset = DefaultValue.objects.all()
    filterset_class = DefaultValueFilter
    permission_classes = [HasGroupPermission]
    serializer_class = DefaultValueSerializer

