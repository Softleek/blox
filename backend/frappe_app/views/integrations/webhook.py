from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.webhook import Webhook
from frappe_app.filters.integrations.webhook import WebhookFilter
from frappe_app.serializers.integrations.webhook import WebhookSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebhookViewSet(GenericViewSet):
    queryset = Webhook.objects.all()
    filterset_class = WebhookFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebhookSerializer

