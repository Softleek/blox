from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.webhook_request_log import WebhookRequestLog

class WebhookRequestLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebhookRequestLog
        fields = '__all__'
