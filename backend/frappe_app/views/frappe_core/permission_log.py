from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.permission_log import PermissionLog
from frappe_app.filters.frappe_core.permission_log import PermissionLogFilter
from frappe_app.serializers.frappe_core.permission_log import PermissionLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PermissionLogViewSet(GenericViewSet):
    queryset = PermissionLog.objects.all()
    filterset_class = PermissionLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PermissionLogSerializer

