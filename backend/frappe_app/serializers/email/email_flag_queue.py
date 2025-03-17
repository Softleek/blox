from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_flag_queue import EmailFlagQueue

class EmailFlagQueueSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailFlagQueue
        fields = '__all__'
