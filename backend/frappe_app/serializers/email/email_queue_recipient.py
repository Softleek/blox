from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_queue_recipient import EmailQueueRecipient

class EmailQueueRecipientSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailQueueRecipient
        fields = '__all__'
