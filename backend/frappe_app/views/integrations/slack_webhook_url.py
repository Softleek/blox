from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.slack_webhook_url import SlackWebhookURL
from frappe_app.filters.integrations.slack_webhook_url import SlackWebhookURLFilter
from frappe_app.serializers.integrations.slack_webhook_url import SlackWebhookURLSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class SlackWebhookURLViewSet(GenericViewSet):
    queryset = SlackWebhookURL.objects.all()
    filterset_class = SlackWebhookURLFilter
    permission_classes = [HasGroupPermission]
    serializer_class = SlackWebhookURLSerializer

