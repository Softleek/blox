from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.frappe_core.sms_log import SMSLog
from frappe_app.filters.frappe_core.sms_log import SMSLogFilter
from frappe_app.serializers.frappe_core.sms_log import SMSLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SMSLogViewSet(GenericViewSet):
    queryset = SMSLog.objects.all()
    filterset_class = SMSLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SMSLogSerializer

