from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.push_notification_settings import PushNotificationSettings

class PushNotificationSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = PushNotificationSettings
        fields = '__all__'
