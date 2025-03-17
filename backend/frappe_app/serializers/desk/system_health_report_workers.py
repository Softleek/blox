from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_health_report_workers import SystemHealthReportWorkers

class SystemHealthReportWorkersSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemHealthReportWorkers
        fields = '__all__'
