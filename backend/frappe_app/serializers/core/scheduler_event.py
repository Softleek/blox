from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.core.scheduler_event import SchedulerEvent

class SchedulerEventSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SchedulerEvent
        fields = '__all__'
