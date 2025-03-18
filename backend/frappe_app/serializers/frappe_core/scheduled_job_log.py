from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.scheduled_job_log import ScheduledJobLog

class ScheduledJobLogSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ScheduledJobLog
        fields = '__all__'
