from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.view_log import ViewLog
from frappe_app.filters.core.view_log import ViewLogFilter
from frappe_app.serializers.core.view_log import ViewLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class ViewLogViewSet(GenericViewSet):
    queryset = ViewLog.objects.all()
    filterset_class = ViewLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = ViewLogSerializer

