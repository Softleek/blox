from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.error_log import ErrorLog
from frappe_app.filters.frappe_core.error_log import ErrorLogFilter
from frappe_app.serializers.frappe_core.error_log import ErrorLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ErrorLogViewSet(GenericViewSet):
    queryset = ErrorLog.objects.all()
    filterset_class = ErrorLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ErrorLogSerializer

