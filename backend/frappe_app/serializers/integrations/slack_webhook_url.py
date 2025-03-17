from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.slack_webhook_url import SlackWebhookURL

class SlackWebhookURLSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SlackWebhookURL
        fields = '__all__'
