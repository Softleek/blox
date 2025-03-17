from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.notification_log import NotificationLog

class NotificationLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NotificationLog
        fields = '__all__'
