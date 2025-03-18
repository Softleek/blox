from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.activity_log import ActivityLog
from frappe_app.filters.frappe_core.activity_log import ActivityLogFilter
from frappe_app.serializers.frappe_core.activity_log import ActivityLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ActivityLogViewSet(GenericViewSet):
    queryset = ActivityLog.objects.all()
    filterset_class = ActivityLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ActivityLogSerializer

