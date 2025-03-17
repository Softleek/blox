from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.webhook_request_log import WebhookRequestLog
from frappe_app.filters.integrations.webhook_request_log import WebhookRequestLogFilter
from frappe_app.serializers.integrations.webhook_request_log import WebhookRequestLogSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebhookRequestLogViewSet(GenericViewSet):
    queryset = WebhookRequestLog.objects.all()
    filterset_class = WebhookRequestLogFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebhookRequestLogSerializer

