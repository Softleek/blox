from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_console import SystemConsole

class SystemConsoleSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemConsole
        fields = '__all__'
