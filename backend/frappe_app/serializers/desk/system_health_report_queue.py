from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_health_report_queue import SystemHealthReportQueue

class SystemHealthReportQueueSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemHealthReportQueue
        fields = '__all__'
