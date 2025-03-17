from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.console_log import ConsoleLog

class ConsoleLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ConsoleLog
        fields = '__all__'
