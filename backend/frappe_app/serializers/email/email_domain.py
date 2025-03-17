from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.email.email_domain import EmailDomain

class EmailDomainSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = EmailDomain
        fields = '__all__'
