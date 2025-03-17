from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_unsubscribe import EmailUnsubscribe

class EmailUnsubscribeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailUnsubscribe
        fields = '__all__'
