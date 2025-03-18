from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.sms_settings import SMSSettings
from frappe_app.filters.frappe_core.sms_settings import SMSSettingsFilter
from frappe_app.serializers.frappe_core.sms_settings import SMSSettingsSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SMSSettingsViewSet(GenericViewSet):
    queryset = SMSSettings.objects.all()
    filterset_class = SMSSettingsFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SMSSettingsSerializer

