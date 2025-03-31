from core.views.template import GenericViewSet, SingleInstanceViewSet
from frappe_app.models.frappe_core.session_default_settings import SessionDefaultSettings
from frappe_app.filters.frappe_core.session_default_settings import SessionDefaultSettingsFilter
from frappe_app.serializers.frappe_core.session_default_settings import SessionDefaultSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SessionDefaultSettingsViewSet(SingleInstanceViewSet):
    queryset = SessionDefaultSettings.objects.all()
    permission_classes = [HasGroupPermission]
    serializer_class = SessionDefaultSettingsSerializer

    filterset_class = SessionDefaultSettingsFilter
