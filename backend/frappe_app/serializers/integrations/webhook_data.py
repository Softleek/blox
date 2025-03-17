from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.webhook_data import WebhookData

class WebhookDataSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = WebhookData
        fields = '__all__'
