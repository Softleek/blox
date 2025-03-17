from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.logs_to_clear import LogsToClear

class LogsToClearSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = LogsToClear
        fields = '__all__'
