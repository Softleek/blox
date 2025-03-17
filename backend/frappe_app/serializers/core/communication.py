from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.communication import Communication

class CommunicationSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = '__all__'
