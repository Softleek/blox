from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_queue import EmailQueue

class EmailQueueSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailQueue
        fields = '__all__'
