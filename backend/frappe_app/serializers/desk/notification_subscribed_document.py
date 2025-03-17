from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.notification_subscribed_document import NotificationSubscribedDocument

class NotificationSubscribedDocumentSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = NotificationSubscribedDocument
        fields = '__all__'
