from rest_framework import serializers
from core.serializers.template import RelationshipHandlerMixin
from frappe_app.models.desk.system_health_report_errors import SystemHealthReportErrors

class SystemHealthReportErrorsSerializer(RelationshipHandlerMixin, serializers.ModelSerializer):

    class Meta:
        model = SystemHealthReportErrors
        fields = '__all__'
