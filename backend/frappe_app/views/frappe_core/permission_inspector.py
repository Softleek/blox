from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.permission_inspector import PermissionInspector
from frappe_app.filters.frappe_core.permission_inspector import PermissionInspectorFilter
from frappe_app.serializers.frappe_core.permission_inspector import PermissionInspectorSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PermissionInspectorViewSet(GenericViewSet):
    queryset = PermissionInspector.objects.all()
    filterset_class = PermissionInspectorFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PermissionInspectorSerializer

