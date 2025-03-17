from rest_framework import viewsets
from core.views.template import GenericViewSet
from frappe_app.models.integrations.webhook_data import WebhookData
from frappe_app.filters.integrations.webhook_data import WebhookDataFilter
from frappe_app.serializers.integrations.webhook_data import WebhookDataSerializer
from rest_framework.permissions import AllowAny
from core.permissions import HasGroupPermission

class WebhookDataViewSet(GenericViewSet):
    queryset = WebhookData.objects.all()
    filterset_class = WebhookDataFilter
    permission_classes = [HasGroupPermission]
    serializer_class = WebhookDataSerializer

