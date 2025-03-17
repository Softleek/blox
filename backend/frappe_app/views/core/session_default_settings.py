from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.core.session_default_settings import SessionDefaultSettings
from frappe_app.filters.core.session_default_settings import SessionDefaultSettingsFilter
from frappe_app.serializers.core.session_default_settings import SessionDefaultSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SessionDefaultSettingsViewSet(GenericViewSet):
    queryset = SessionDefaultSettings.objects.all()
    filterset_class = SessionDefaultSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SessionDefaultSettingsSerializer

