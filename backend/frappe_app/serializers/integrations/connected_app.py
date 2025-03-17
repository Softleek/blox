from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.integrations.connected_app import ConnectedApp

class ConnectedAppSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ConnectedApp
        fields = '__all__'
