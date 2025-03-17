from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_account import EmailAccount

class EmailAccountSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailAccount
        fields = '__all__'
