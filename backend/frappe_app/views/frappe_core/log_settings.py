from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.log_settings import LogSettings
from frappe_app.filters.frappe_core.log_settings import LogSettingsFilter
from frappe_app.serializers.frappe_core.log_settings import LogSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LogSettingsViewSet(GenericViewSet):
    queryset = LogSettings.objects.all()
    filterset_class = LogSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = LogSettingsSerializer

