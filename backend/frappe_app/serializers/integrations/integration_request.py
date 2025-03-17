from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.integration_request import IntegrationRequest

class IntegrationRequestSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = IntegrationRequest
        fields = '__all__'
