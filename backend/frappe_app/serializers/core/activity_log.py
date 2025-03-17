from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.activity_log import ActivityLog

class ActivityLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ActivityLog
        fields = '__all__'
