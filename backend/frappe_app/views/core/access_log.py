from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.access_log import AccessLog
from frappe_app.filters.core.access_log import AccessLogFilter
from frappe_app.serializers.core.access_log import AccessLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class AccessLogViewSet(GenericViewSet):
    queryset = AccessLog.objects.all()
    filterset_class = AccessLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = AccessLogSerializer

