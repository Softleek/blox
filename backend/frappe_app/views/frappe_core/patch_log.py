from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.patch_log import PatchLog
from frappe_app.filters.frappe_core.patch_log import PatchLogFilter
from frappe_app.serializers.frappe_core.patch_log import PatchLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class PatchLogViewSet(GenericViewSet):
    queryset = PatchLog.objects.all()
    filterset_class = PatchLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = PatchLogSerializer

