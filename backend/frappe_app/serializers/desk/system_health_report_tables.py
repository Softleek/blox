from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_health_report_tables import SystemHealthReportTables

class SystemHealthReportTablesSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemHealthReportTables
        fields = '__all__'
