from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.webhook_header import WebhookHeader

class WebhookHeaderSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebhookHeader
        fields = '__all__'
