from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.webhook import Webhook

class WebhookSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Webhook
        fields = '__all__'
