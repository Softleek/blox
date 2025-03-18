from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.error_log import ErrorLog

class ErrorLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ErrorLog
        fields = '__all__'
