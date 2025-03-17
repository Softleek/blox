from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.notification_settings import NotificationSettings

class NotificationSettingsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NotificationSettings
        fields = '__all__'
