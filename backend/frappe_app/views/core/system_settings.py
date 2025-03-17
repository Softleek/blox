from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.system_settings import SystemSettings
from frappe_app.filters.core.system_settings import SystemSettingsFilter
from frappe_app.serializers.core.system_settings import SystemSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SystemSettingsViewSet(GenericViewSet):
    queryset = SystemSettings.objects.all()
    filterset_class = SystemSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SystemSettingsSerializer

