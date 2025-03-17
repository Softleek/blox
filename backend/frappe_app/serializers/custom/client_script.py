from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.custom.client_script import ClientScript

class ClientScriptSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ClientScript
        fields = '__all__'
