from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.notification_recipient import NotificationRecipient

class NotificationRecipientSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NotificationRecipient
        fields = '__all__'
