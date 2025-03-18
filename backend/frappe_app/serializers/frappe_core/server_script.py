from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.server_script import ServerScript

class ServerScriptSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ServerScript
        fields = '__all__'
