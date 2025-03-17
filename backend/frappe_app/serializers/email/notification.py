from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.notification import Notification

class NotificationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
