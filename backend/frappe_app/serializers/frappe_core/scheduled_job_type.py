from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.frappe_core.scheduled_job_type import ScheduledJobType

class ScheduledJobTypeSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = ScheduledJobType
        fields = '__all__'
