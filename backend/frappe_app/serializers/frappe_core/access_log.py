from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.access_log import AccessLog

class AccessLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = AccessLog
        fields = '__all__'
