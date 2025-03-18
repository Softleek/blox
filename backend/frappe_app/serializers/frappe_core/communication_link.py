from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.communication_link import CommunicationLink

class CommunicationLinkSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = CommunicationLink
        fields = '__all__'
