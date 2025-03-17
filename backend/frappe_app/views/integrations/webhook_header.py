from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.webhook_header import WebhookHeader
from frappe_app.filters.integrations.webhook_header import WebhookHeaderFilter
from frappe_app.serializers.integrations.webhook_header import WebhookHeaderSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebhookHeaderViewSet(GenericViewSet):
    queryset = WebhookHeader.objects.all()
    filterset_class = WebhookHeaderFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebhookHeaderSerializer

