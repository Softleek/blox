from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.log_settings import LogSettings
from frappe_app.filters.frappe_core.log_settings import LogSettingsFilter
from frappe_app.serializers.frappe_core.log_settings import LogSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class LogSettingsViewSet(SingleInstanceViewSet):
    queryset = LogSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = LogSettingsSerializer

    filterset_class = LogSettingsFilter
